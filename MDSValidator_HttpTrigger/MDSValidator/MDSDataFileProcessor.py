import os
import sys
import csv
from time import time
from datetime import datetime

from .logger import logger
from .AOD_MDS.helpers import read_data, read_header

from .rule_checker.JSONValidator import JSONValidator
from .rule_checker.MJValidationError import MJValidationError
from .utils.files import get_latest_data_file, get_result_filename
from .utils.dates import get_period, Period
from .utils.output_helpers import get_vresult_rows
#from utils.log import log_results
from .rule_checker.constants import MODE_LOOSE
from .utils.InputFileErrors import MissingHeadersError, NoDataError
from .Providers import SchemaProvider, FileSchemaProvider  # CosmosMongo, SchemaProvider
from ..CommonUtils.AZTableService import AZTableService
from .AOD_MDS.MDSConfig import MDSLocalConfigurationLoader

#import pprint

"""
    This module is to be made responsible for being the engine for orchestrating, the processing of incoming JSON data.
    1. Queue up a task for :
        a. pushing the data as-is into the database with timestamp etc.
        b. then reading it for cleansing and validation (including determining suggestions for SLK, and other values)
        c. writing the errors and warnings to the database
        d. returning the errors and warnings to the caller/client
    2. Queue up a 2nd task after 1.c, to write to excel file with color coded formatting
        then return the path to the new .xlsx to the user.
"""

# def get_json_validator(period: Period, program=''):
#   schema_obj = schema.schema
#   return JSONValidator(schema_obj ,period, program=program)

# map period to schema version date , then load schema with key : "Program_SchemaVersion" e.g. TSS_052019 => "AMDS_v07-2019"


def get_schema_schemadomain(schema_provider: SchemaProvider, period: Period, program):
    
    main_schema, definitions = schema_provider.build_schema()
    return main_schema, definitions, schema_provider.schema_domain
    

def get_validator(main_schema, definitions, period, program, addnl_config):
  
    jv = JSONValidator(main_schema, definitions, addnl_config,
                       period, program=program)
    return jv


def get_valid_header(data_header_row, validator, mode):
    missing_headers, fixed_header, header_warnings = \
        validator.validate_header(data_header_row, mode=mode)
    if missing_headers:
        logger.error(
            f"Missing Headers {missing_headers} \n warnings {header_warnings}")
        raise MissingHeadersError(
            str(missing_headers), "Missing headers in input file")

    return fixed_header, header_warnings


def get_data(data, mds_header, open_and_closed_eps=None):

    data = read_data(data[1:], mds_header,
                     open_and_closed_eps=open_and_closed_eps)
    if not data or not data['episodes'] or len(data['episodes']) < 1:
        logger.critical("No data. Quitting...")
        raise NoDataError("missing episodes", "No data in input file")

    return data


# @click.command()
# @click.option('--data_file', '-d',
#               help='Default: use the latest .csv file in the input folder.')
# @click.option('--all_eps/--closed_only', '-a/-c', default=True,
#               help='Validate only closed episodes. Default is to validate all episodes',
#               show_default=True)
# @click.option('--errors_only', '-e', help='Output only the rows with errors.', default=False,
#                 show_default=True, type=click.BOOL)
# @click.option('--start_date', '-t', type=click.DateTime(formats=["%Y-%m-%d"]),
#               help='The number of the starting month of the reporting period . Eg.: 2019-07-01',
#               required=False)
# @click.option('--program', '-p', type=click.Choice(['TSS', 'Arcadia-Resi', 'Althea', 'Other']),
#               help='Some logic rules are specific to a team.' + \
#                     'Default setting is to just apply just MDS rules.',
#               default='TSS', show_default=True)
# @click.option('--reporting_period', '-r', type=click.Choice(["12", "6", "3", "1"]),
#               help='reporting period window.',
#               default="3", show_default=True)
# @click.option('--nostrict/--strict', '-s/-S', default=False,
#               help='Accept/Reject imperfect data files with known aliases.' +
#                    '\n1: reject (flag as errors)', show_default=True)
def main(data, open_and_closed_eps, errors_only, start_date,
         program='TSS', reporting_period=1, nostrict=False):
    if not start_date:
        start_date = datetime(2020, 1, 1)
        logger.warn(
            f"No start date was passed in - defaulting to 1 July 2020 {start_date}")

    result_dicts = exe(data, open_and_closed_eps, errors_only,
                       start_date, program=program,
                       period=reporting_period, nostrict=nostrict)

    logger.info("\t ...End of Program...\n")
    return result_dicts


def _split_strings_to_cols(data):
    cr = csv.reader(data, skipinitialspace=True)
    return [row for row in cr]


def exe(data, open_and_closed_eps, errors_only, start_date,
        program='TSS', period=1, nostrict=False):

    start_time = time()

    period = get_period(start_date, period_months=period)
    schema_provider = FileSchemaProvider.FileSchemaProvider(period.start, program)
    main_schema, definitions = schema_provider.build_schema()


    table_service = AZTableService("MDSValidatorMappings")

    config_loader = MDSLocalConfigurationLoader(table_service.table_client)
    
    # aliases & matrix of drugs
    addnl_config = config_loader.get_config(schema_provider.schema_domain)
    jv = JSONValidator(main_schema, definitions, addnl_config,
                       period, program=program)
    # map period to schema version date , then load schema with key : "Program_SchemaVersion" e.g. TSS_052019 => "ACTMDS_v07-2019"

    data = _split_strings_to_cols(data)

    # fix and rename the headers
    header_row = (str.lower(h) for h in data[0])
    mds_header, _ = get_valid_header(header_row, validator=jv, mode=nostrict)

    data = get_data(data, mds_header, open_and_closed_eps=open_and_closed_eps)

    verrors, _ = jv.validate(data, mode=nostrict)

    end_time = time()
    logger.info(
        f"\n\t ...End of validation... \n\t Processing time {round(end_time - start_time,1)} seconds.")

    # this is to enforce order regardless of what order the columns are in the input file
    # and
    #   ? to match the error excel template headers
    # TODO : load from schema file.
    template_column_headers = {'ACTMDS': ['enrolling provider', 'id', 'first name', 'surname', 'eid', 'slk 581', 'sex',
                                          'dob', 'date accuracy indicator', 'country of birth', 'indigenous status',
                                          'preferred language', 'postcode (australian)', 'usual accommodation', 'client type',
                                          'source of referral', 'commencement date', 'end date', 'reason for cessation',
                                          'treatment delivery setting', 'method of use for pdc', 'injecting drug use status',
                                          'principle drug of concern', 'odc1', 'odc2', 'odc3', 'odc4', 'odc5',
                                          'main treatment type', 'ott1', 'ott2', 'ott3', 'ott4', 'living arrangements',
                                          'previous alcohol and other drug treatment received', 'mental health'],
                               'NSWMDS': [
        # <<< --- staff info useful when returning it to staff to fix.
        'staff', 'location', 'service',
        #         Location and service to encode for nadabase upload
        'id', 'first name', 'surname', 'slk 581', 'sex', 'dob',
        'date accuracy indicator', 'country of birth', 'indigenous status', 'preferred language',
        'postcode (australian)', 'usual accommodation', 'client type', 'source of referral',
                                 'principal source of income',  # <<< ---
                                 'commencement date', 'end date', 'reason for cessation',
                                 'referral to another service',  # <<< ---
                                 'treatment delivery setting', 'method of use for pdc',
                                 'injecting drug use status', 'principle drug of concern', 'odc1', 'odc2', 'odc3', 'odc4',
                                 'odc5', 'main treatment type', 'ott1', 'ott2', 'ott3', 'ott4', 'living arrangements',
                                 'previous alcohol and other drug treatment received', 'mental health'
    ]
    }

    rows = get_vresult_rows(template_column_headers[schema_provider.schema_domain],
                            len(template_column_headers), data['episodes'], verrors)
    logger.info("\t ...result ..{rows}\n")

    return rows

# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))

# # 0 - 9
# 'EID','Person identifier','Sex','DOB','Country of birth','Indigenous status','Preferred language','Client type','Source of referral',
# # 10 - 12
# 'Date of commencement of treatment episode for alcohol and other drugs','Date of cessation of treatment episode for alcohol and other drugs','Reason for cessation',
# # 13 -22
# 'Treatment delivery setting','Method of use for PDC','Injecting drug use status','Principal drug of concern','ODC1','ODC2','ODC3','ODC4','ODC5','Main treatment type',
# #  23 -32
# 'OTT1','OTT2','OTT3','OTT4','Date accuracy indicator','SLK 581','Postcode (Australian)','Usual accommodation','Living arrangements','Previous AOD treatment',

# #33
# 'Mental health (Diagnosed with a mental illness)',

# # 34, 35, 36
# 'Medicine received alongside the main treatment type - opioid overdose reversal',
# 'Medicine received alongside the main treatment type - nicitone replacement therapy','Medicine received alongside the main treatment type - hepatitis C treatment'
