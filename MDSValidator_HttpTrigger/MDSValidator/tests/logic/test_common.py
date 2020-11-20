
#import os
#from datetime import datetime as dt
import pytest
import copy

from . import noerrors_base_translated, noerrors_base_nsw_translated, get_validator


@pytest.fixture(scope="module")
def ACT_json_validator():
  validator, _ = get_validator('TSS')
  return validator

@pytest.fixture(scope="module")
def NSW_json_validator():
  validator, _ = get_validator ('Pathways')
  return validator


@pytest.mark.parametrize("client_id, end_date, cess_reason,  error", [
                          ('11525',  '', 'treatment completed', 
                            [{'cid': '11525', 'etype': 'logic',
                             'field': 'reason for cessation', 'index': 0,
                             'message': 'end date and reason for cessation should be present together'}]                            
                          )
                        ,
                          ('4353', "9/06/2020", '', [
                              {'cid': '4353', 'etype': 'logic', 
                              'field': 'reason for cessation', 'index': 0,
                              'message': 'end date and reason for cessation should be present together'}])
                        ])
def test_act_field_dependencies(ACT_json_validator, client_id, end_date, cess_reason, error):
        
        base4error = copy.deepcopy(noerrors_base_translated)
        
        base4error['id'] = client_id
        base4error['end date'] = end_date
        base4error['reason for cessation'] = cess_reason
            
        errors, _ = ACT_json_validator.validate({'episodes' :[base4error]})
        assert errors[0] == error


@pytest.mark.parametrize("client_id, end_date, cess_reason, ref_ano_svc, error", [
                         ('11525',  "", "service completed", "general practitioner", [                          
                            {'cid': '11525', 'etype': 'logic',                     # PASS 1
                             'field': 'reason for cessation', 'index': 0,
                             'message': 'end date and reason for cessation should be present together'}
                             ,
                            {'cid': '11525', 'etype': 'logic',                     
                             'field': 'referral to another service', 'index': 0, 
                             'message': 'end date and referral to another service should be present together'}
                         ])
                          ,
                         
                        ('4353', "9/06/2020", "", "general practitioner", [                        
                              {'cid': '4353', 'etype': 'logic',                # PASS 2
                                'field': 'reason for cessation', 'index': 0,
                                'message': 'end date and reason for cessation should be present together'}                                                    
                              ])
                        ])
def test_nsw_field_dependencies(NSW_json_validator, client_id, end_date, cess_reason, ref_ano_svc, error):
        
        base4error = copy.deepcopy(noerrors_base_nsw_translated)
        
        base4error['id'] = client_id
        base4error['end date'] = end_date
        base4error['reason for cessation'] = cess_reason
        base4error['referral to another service'] = ref_ano_svc
        
        
        errors, _ = NSW_json_validator.validate({'episodes' :[base4error]})
        assert errors[0] == error