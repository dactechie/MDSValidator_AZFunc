
import pytest
#from AOD_MDS.helpers import  translate_to_MDS_header, translate_to_MDS_values
from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.constants import MDS as M
from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.helpers.translators import (fields_map, headers_map, 
            translate_to_MDS_header, translate_to_MDS_values)
from MDSValidator_HttpTrigger.MDSValidator.logger import logger



# pytest  tests/test_helpers.py::test_translate_to_MDS_header -vv
@pytest.mark.parametrize("header, expected", 
                          [( # ["pid", "method of use for principal drug of concern" ],["id", "method of use for pdc"],
                            [ # NSW MDS spreadsheet headers
                              "pid",	"last name",	"first name",	"slk 581",	"sex",	"date of birth",	"date accuracy indicator (for dob)",	"country of birth",	"indigenous status",
                              "preferred language",	"postcode - australian",	"usual accommodation",	"client type",	"source of referral",	"principal source of income",	"commencement date",
                              "end date",	"reason for cessation",	"referral to another service",	"treatment delivery setting",	"method of use for principal drug of concern",	"injecting drug status",
                              "pdc",	"main treatment type (mtt)",	"living arrangements",	"previous aod treatment",	
                              "mental health (diagnosed with a mental illness)"],

                              #  Expected : from constants:
                              ["id", "surname", "first name", "slk 581", "sex",	'dob', "date accuracy indicator", "country of birth", "indigenous status",
                              "preferred language", "postcode (australian)",
                              "usual accommodation",	"client type", "source of referral", "principal source of income","commencement date",
                              "end date",	"reason for cessation", "referral to another service" , "treatment delivery setting", "method of use for pdc",
                              "injecting drug use status", "principle drug of concern",	"main treatment type",	"living arrangements",	
                              "previous alcohol and other drug treatment received", "mental health"]                                	                            
                          )]
                        )
def test_translate_to_MDS_header(header, expected):    
    converted_header, warnings = translate_to_MDS_header(header)
    logger.info(warnings)
    assert converted_header == expected


@pytest.mark.parametrize("data, expected, expected_warnings", 
                          [( # testing the field_values map as well..
                            [{ 'id': '101010',  'client type': "own drug use" }], 
                            {'client type':"own alcohol or other drug use", 'id': '101010'}, 
                            { "index": 0, "cid": '101010', "required": "own alcohol or other drug use", "got": "own drug use"}
                          ),
                          ( [{ 'id': '12354',  'client type': "other's drug use" }], 
                            {'client type':"other's alcohol or other drug use", 'id': '12354'}, 
                            { "index": 0, "cid": '12354', "required": fields_map[M['CLNT_TYP']]["other's drug use"],
                              "got": "other's drug use"}
                          )
                        ])
def test_translate_to_MDS_values(data, expected, expected_warnings):
    warnings = translate_to_MDS_values(data)
    logger.info(warnings)

    assert data[0] == expected
    
    assert warnings[0] == expected_warnings
