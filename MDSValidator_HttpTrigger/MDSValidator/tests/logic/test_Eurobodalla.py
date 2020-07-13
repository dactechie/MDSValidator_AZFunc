
#import os
#from datetime import datetime as dt
import pytest
import copy
from ...AOD_MDS.constants import MDS as M

from . import noerrors_base_nsw_translated, period, get_validator

S_MTT_PHARM = "invalid value/format: 'pharmacotherapy'"
ex_tds = { 'etype': 'enum', 'field': M['MTT']}
error = { 'index': 0 ,'cid': '',  **ex_tds, 'message': S_MTT_PHARM}


@pytest.fixture(scope="module")
def Euro_json_validator():
  return get_validator ('PathwaysEurobodalla')


@pytest.mark.parametrize("client_id, mtt, ott1, err", [
                                          ('11525',  'support and case management only', '', {}),
                                          #  ('4353', 'information and education', '', {}),
                                          ('343','pharmacotherapy', '', error),
                                          # ('11526','pharmacotherapy', 'support and case management', {}),
                                          # ('11525','support and case management', 'pharmacotherapy', {}),
                                          ])
def test_no_treat(Euro_json_validator, client_id, mtt, ott1, err):
  base1_error = copy.deepcopy(noerrors_base_nsw_translated)
  base1_error[M['MTT']] =  mtt
  base1_error['ott1'] =  ott1
  base1_error['id'] = client_id

  if err:
    err['cid'] = client_id
  
  errors, _ = Euro_json_validator.validate({'episodes' :[base1_error]})
  

  assert (not err and len(errors[0]) == 0)  or errors[0][0] == err
  

