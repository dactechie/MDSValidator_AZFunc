#import os
import pytest
import pytest_dependency
import copy
#from AOD_MDS.constants import MDS as M, MDS_Dates as D


from collections import OrderedDict
from ...AOD_MDS.schema import schema

#from  MDSValidator.rule_checker import  
from . import JSONValidator, noerrors_base, noerrors_base_translated, period


@pytest.fixture(scope="module")
def json_validator():    
    return JSONValidator(schema.schema, period=period, program=None)


@pytest.mark.dependency() 
def test_header_noerrors(json_validator):
  header = list(noerrors_base)
  missing_headers, fixed_header, header_warnings = json_validator.validate_header(header, mode=False)
  expected_header = ['id','first name','surname','slk 581','dob','sex','date accuracy indicator','country of birth','indigenous status','preferred language',
    'client type','source of referral','commencement date','end date','reason for cessation','treatment delivery setting','method of use for pdc',
    'injecting drug use status','principle drug of concern','odc1','odc2','odc3','odc4','odc5','main treatment type','ott1','ott2','ott3','ott4',
    'postcode (australian)','living arrangements','usual accommodation','previous alcohol and other drug treatment received','mental health']


  assert expected_header == fixed_header
  assert   {'pat id': 'id', 'first name' : 'first name', 
      'slk581':  'slk 581', 'sex': 'sex', 'dob accuracy': 'date accuracy indicator', 'country': 'country of birth', 'indig status': 'indigenous status', 'language': 'preferred language',
       'client': 'client type', 'source': 'source of referral', 'enrolment': 'commencement date', 'discharge': 'end date', 'cessation':'reason for cessation', 'setting': 'treatment delivery setting',
       'use':'method of use for pdc', 'injection':'injecting drug use status', 'drug': 'principle drug of concern', 'treat': 'main treatment type', 'postcode': 'postcode (australian)', 
       'living': 'living arrangements', 'accom': 'usual accommodation', 'previous treatment': 'previous alcohol and other drug treatment received', 
       'mental health': 'mental health'} ==   header_warnings


  assert len(missing_headers) == 0, "the list is not empty" # empty list



# @pytest.mark.dependency(depends=["test_header_noerrors"])
# def test_data_noerrors(json_validator):
#         errors, _ = json_validator.validate({'episodes' : [noerrors_base_translated]})
    
#         expected = []        
#         assert errors[0] == expected


# def test_out_of_period(json_validator):
#   baseerror = copy.deepcopy(noerrors_base_translated)
#   baseerror['commencement date'] = '01/01/2017'
#   baseerror['end date'] ='01/01/2020'
#   baseerror['id'] ='7777'
#   input = [baseerror]

#   errors, _ = json_validator.validate({'episodes' :input})

#   expected4 = [{'cid': '7777',  'etype': 'logic','field': 'end date',
#                 'index': 0, 'message': 'Episode End Date is not in the reporting period'
#                 }]

#   assert errors[0] == expected4