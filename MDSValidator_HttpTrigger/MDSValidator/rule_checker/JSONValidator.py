from ..utils import remove_unicode
import json
import copy
from datetime import date
import jsonschema as jsc

from ..json_logic import add_operation, jsonLogic
from ..AOD_MDS.helpers import (prep_and_check_overlap,
                               fix_check_dates,
                               fuse_suggestions_into_errors, getSLK,
                               translate_to_MDS_header,
                               translate_to_MDS_values, is_valid_drug_use)  # , can_process_withdates)
from ..AOD_MDS.constants import MDS, MDS_Dates, MDS_ST_FLD, MDS_END_FLD
from ..AOD_MDS.logic_rules.common import rule_definitions as common_rules
from ..AOD_MDS.logic_rules import get_program_rules
from ..utils import (cleanse_string, get_date_converter, has_duplicate_values,
                     has_gaps, compile_logic_errors, remove_vrules,
                     add_error_obj, Period, in_period)
from ..utils.InputFileErrors import SchemaValidationError
from ..logger import logger
from .MJValidationError import MJValidationError
from .constants import MODE_LOOSE, NOW_ORD, NOW
from ...CommonUtils import constants as DBConstants


'''
Create a validation error object with the data row index, client id and error details.
'''


def header_er_lam(field, miss_extra): return MJValidationError(index='all',
                                                               cid='all',
                                                               etype='field',
                                                               field=field,
                                                               message=miss_extra)


def clean_headers(header):
    return [remove_unicode(dh) for dh in header]


class JSONValidator(object):

    def __init__(self, schema_obj, definitions, addnl_config, period: Period, program):
        self.validator = JSONValidator.setup_validator(schema_obj, definitions)
        self.schema = schema_obj
        self.period = period

        self.aliases = addnl_config.get(DBConstants.DB_KEY_ALIASES)
        self.method_of_use_matrix = addnl_config.get(
            DBConstants.DB_KEY_METHOD_MATRIX)

        self.rule_definitions = copy.deepcopy(common_rules)
        self.rules = [r['rule'] for r in self.rule_definitions]

        addnl_def = None
        if program:
          addnl_def = get_program_rules(program)
          if addnl_def:
            self.rule_definitions.extend(addnl_def)
            self.rules.extend([r['rule'] for r in addnl_def])
          else:
           logger.warning(f"{program} program validation not implmented yet, only going to check common rules.")

        self.slk_suggestions = {}

    """
      schema_refd_objects [ 'atsi' : []  , ]   
                            #atsi enum
    """
    # @staticmethod
    # def _custom_schema_resolver(schema, schema_refd_objects):

    #   schema_props = schema['definitions']['episode']['properties']

    #   ref_items =[var for var in schema_props if "$ref" in var]

    @staticmethod
    def setup_validator(schemaObj, definitions):
        validator = jsc.Draft4Validator(schemaObj)  # , resolver=resolver)
        validator.resolver.store['/defs.json'] = definitions
        return validator

    # @staticmethod
    # def setup_validator(schema_dir, schema_file_name):
    #     validator = None
    #     with open(schema_file_name) as schemaFile:
    #         schemaObj = json.load(schemaFile)
    #         resolver = jsc.RefResolver('file:///' + schema_dir, schemaObj)
    #         validator = jsc.Draft4Validator(schemaObj, resolver=resolver)

    #     return validator, schemaObj

    # TODO : schema validation may have already deduced that dates, etc may be invalid.
    #        those errors  would contain the rec_index of the error too

    def validate_logic(self, errors, data_row, rec_idx, date_conversion_errors,
                       id_field, client_eps):
        """
        1. Checks the date format and converts dates into integer ('ordinal's) for easy comparison.
        2. Checks MDS business logic defined in MDS_RULES.py (and imported in the global 'rule_definitions').
            For example EPISODEs OVERLAP.(See 'ACT MDS Data Collection Guide' document for suggested logic checks)

        3. If there errors in the date formats, all the logic checks (for the passed-in data row),
            that involve the malformed dates are excluded.
           The errors from these validations are added to the 'errors' array that is passed in.

        4. client_eps : This is an (on-going) accumulated list of the start and end dates of the
            passed-in client's episodes. This allows us to calculate episode overlaps with the current data row.
        """

        temp_rd = self.rule_definitions
        temp_rules = self.rules
        dce_fields = []
        if any(date_conversion_errors):
            dce_fields = [dce['field'] for dce in date_conversion_errors]
            temp_rd = remove_vrules(dce_fields)
            temp_rules = [rd['rule'] for rd in temp_rd]

        result = [jsonLogic(r, data_row) for r in temp_rules]

        logic_errors = compile_logic_errors(result, temp_rd, data_row,
                                            rec_idx, id_field, date_conversion_errors)
        if rec_idx not in errors:
            errors[rec_idx] = logic_errors
        elif logic_errors:
            errors[rec_idx].extend(logic_errors)

        prep_and_check_overlap(data_row, client_eps,
                               errors, rec_idx, dce_fields)

        # 'OCommencement Date' is a made-up field that contains the ordinal version of the date
        #  to be used for easy comparison (overlap).

        # if there was no error in the commencement and end dates
        # prep_overlap

        # return compile_logic_errors(result, data_row, rec_idx, id_field, date_conversion_errors)

    def validate_header(self, header, mode=MODE_LOOSE):
        warnings = None

        # TODO generate warnings if not clean
        tr_header = clean_headers(header)
        if mode == MODE_LOOSE:
            tr_header, warnings = translate_to_MDS_header(
                tr_header, self.aliases['headers'])

        schema_headers = set(self.schema['definitions']['episode']['required'])
        missing_headers = schema_headers.difference(set(tr_header))

        return missing_headers, tr_header, warnings

        # return [header_er_lam(field=mh, miss_extra='missing field')
        #         for mh in missing_headers], tr_header, warnings

    def check_schema_errors(self, data, id_field):
        errors = {}
        for e in self.validator.iter_errors(data):
            error_code = add_error_obj(errors, e, data, id_field)

            if error_code < 0:  # oneOf fields are missing . Not checked as part of header checks
                if errors and errors[e.path[1]][0]['field'] == '<>':
                    logger.error(f"{errors[e.path[1]][0]['message']}")
                raise SchemaValidationError(errors, "Schema validation error")
        return errors

    # TODO : convert everything to MDS codes first to check numeric values (faster). failed lookups are automatically errors

    def valid_drug_use_method(self, *args):
        return is_valid_drug_use(self.method_of_use_matrix, *args)

    def validate(self, data, mode=MODE_LOOSE):
        """
            The main validator function.
            0. If column headers, dropdown values are not proper MDS values, 
                it looks up a translation dictionary and converts them
            1. If dates (DOB, episode start, end) are not proper dates, it logs ERRORs and 
                excludes the logic validation checks that involve those fields.
            2. Does schema validation using the schema specified in JSON files (schema folder).
            3. Does MDS Logic validation using MDS_RULES.py (jsonLogic)
        """
        warnings = {}
        episodes = data['episodes']
        id_field = MDS['ID']

        if mode == MODE_LOOSE:  # withouth the deep copy of episodes
            # translate to official MDS values
            warnings = translate_to_MDS_values(
                episodes, self.aliases['fields'])
            data = {'episodes': episodes}

        errors = self.check_schema_errors(data, id_field)

        add_operation('has_duplicate_values', has_duplicate_values)
        # change to is_invalid_slk
        add_operation('check_slk', self.check_slk)
        add_operation('has_blanks_in_otherdrugs', has_gaps)
        # change to is_invalid_drug use
        add_operation('is_valid_drug_use', self.valid_drug_use_method)
        add_operation('is_notin_period', self.is_notin_period)

        client_eps = {}

        fn_date_converter = get_date_converter(
            sample_date_str=episodes[0][str.lower(MDS_Dates[0])])

        for i, ep_data in enumerate(episodes):
            date_conversion_errors = fix_check_dates(ep_data, i, fn_date_converter,
                                                     id_field, MDS_Dates)

            self.validate_logic(errors, ep_data, i, date_conversion_errors,
                                id_field, client_eps)
        if self.slk_suggestions:
            fuse_suggestions_into_errors(errors, self.slk_suggestions)

        return errors, warnings

    def is_notin_period(self, episode_end):
        return not in_period(self.period, episode_end)

    def check_slk(self, id, data_slk, firstname, lastname, DOB_str, sex_str):
        must_be = getSLK(firstname, lastname, DOB_str, sex_str)

        if data_slk != must_be:
            self.slk_suggestions[id] = must_be
            return False

        return True

    def check_age(self):
        """
            TODO : Make sure the age is:   10 > age > 100
        """
        pass
