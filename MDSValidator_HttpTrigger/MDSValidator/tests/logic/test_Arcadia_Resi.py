
#import os
#from datetime import datetime as dt
import pytest
import copy
#from  ...AOD_MDS.constants import MDS as M, MDS_Dates as D
from ...AOD_MDS.constants import MDS as M
from . import noerrors_base, noerrors_base_translated, period, get_validator


@pytest.fixture(scope="module")
def Arcadia_Resi_json_validator():
  validator, _ = get_validator('ArcadiaResi')
  return validator


def test_Arcadia_Resi(Arcadia_Resi_json_validator):
  #f"If {M['TDS']} is Residential treatment', '{M['MTT']}' has to be Withdrawal Mgmt.(Detox) / Rehab."
          # Team-based logic: Treatment Delivery Setting
  
  base5error = copy.deepcopy(noerrors_base_translated)
  base5error['treatment delivery setting'] ='residential treatment facility'
  base5error['id'] ='7777'
  input = [base5error]

  errors_arcadia, _ = Arcadia_Resi_json_validator.validate({'episodes' :input})

  expected4 = [
      # {'cid':'4353','etype':'logic','field':'Treatment delivery setting','index': 0,
      # 'message': "TSS team does not provide service (treatment delivery) in Home/'Other' setting "
      # },
      {'cid':'7777','etype':'logic','field':'treatment delivery setting','index': 0,
      'message':  f"If {M['TDS']} is Residential treatment', '{M['MTT']}' has to be Withdrawal Mgmt.(Detox) / Rehab."
      }
  ]

  assert errors_arcadia[0] == expected4