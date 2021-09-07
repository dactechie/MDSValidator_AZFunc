
#import os
#from datetime import datetime as dt
import pytest
import copy
from ...AOD_MDS.constants import MDS as M

from . import noerrors_base_nsw_translated, period, get_validator_for_program



@pytest.fixture(scope="module")
def NSWCCARE_json_validator():
  validator = get_validator_for_program ('Sapphire')
  return validator

# outpatient withdrawal mgt

@pytest.mark.parametrize("client_id, prev_trmt, err", [
                                          ('11525',  'outpatient withdrawal mgt', {}),
                                          #  ('4353', 'information and education', '', {}),
                                          #('343','pharmacotherapy', '', error),
                                          # ('11526','pharmacotherapy', 'support and case management', {}),
                                          # ('11525','support and case management', 'pharmacotherapy', {}),
                                          ])
def test_noerror_prev_trmt(NSWCCARE_json_validator, client_id, prev_trmt, err):
  base1_w_error = copy.deepcopy(noerrors_base_nsw_translated)
  base1_w_error[M['PREV_AOD']] =  prev_trmt
  base1_w_error['id'] = client_id

  if err:
    err['cid'] = client_id
  
  errors, _ = NSWCCARE_json_validator.validate({'episodes' :[base1_w_error]})
  

  assert (not err and len(errors[0]) == 0)  or errors[0][0] == err


  
@pytest.mark.parametrize("client_id, drug, method, err", [
                                          ('11525',  'gambling', 'not collected', {}),
                                          #  ('4353', 'information and education', '', {}),
                                          #('343','pharmacotherapy', '', error),
                                          # ('11526','pharmacotherapy', 'support and case management', {}),
                                          # ('11525','support and case management', 'pharmacotherapy', {}),
                                          ])
def test_nsw_method_of_use_matrix(NSWCCARE_json_validator, client_id, drug, method, err):
  base1_w_error = copy.deepcopy(noerrors_base_nsw_translated)
  base1_w_error[M['PDC']] =  drug
  base1_w_error[M['METHOD']] =  method
  base1_w_error['id'] = client_id

  if err:
    err['cid'] = client_id
  
  errors, _ = NSWCCARE_json_validator.validate({'episodes' :[base1_w_error]})
  

  assert (not err and len(errors[0]) == 0)  or errors[0][0] == err
  

