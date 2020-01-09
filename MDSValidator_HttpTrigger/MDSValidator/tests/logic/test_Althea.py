
#import os
#from datetime import datetime as dt
import pytest
import copy
from ...AOD_MDS.constants import MDS as M
from ...AOD_MDS.schema import schema

from . import  JSONValidator, noerrors_base, noerrors_base_translated, S_PRISON_OUTR, period

S_MTT_PHARM = "If MTT is Pharmacotherapy, OTT1 should be present"
ex_tds = { 'etype': 'logic', 'field': M['MTT']}
error = { 'index': 0 ,'cid': '',  **ex_tds, 'message': S_MTT_PHARM}


@pytest.fixture(scope="module")
def Althea_json_validator():
  # def __init__(self, schema_obj, period: Period, program):
    return JSONValidator(schema.schema, period=period, program='Althea')


@pytest.mark.parametrize("client_id, mtt, ott1, err", [
                                           ('11525',  'support and case management', '', {}),
                                           ('4353', 'information and education', '', {}),
                                           ('343','pharmacotherapy', '', error),
                                          ('11526','pharmacotherapy', 'support and case management', {}),
                                          ('11525','support and case management', 'pharmacotherapy', {}),
                                          ])
def test_no_treat_resi(Althea_json_validator, client_id, mtt, ott1, err):
  base1_error = copy.deepcopy(noerrors_base_translated)
  base1_error[M['MTT']] =  mtt
  base1_error['ott1'] =  ott1
  base1_error['id'] = client_id

  if err:
    err['cid'] = client_id
  
  errors, _ = Althea_json_validator.validate({'episodes' :[base1_error]})
  

  assert (not err and len(errors[0]) == 0)  or errors[0][0] == err
  

