# from ..constants import MDS, MDS_END_FLD, MDS_ST_FLD
# from datetime import datetime
import pytest
import copy
from . import noerrors_base_translated, get_validator_for_program

@pytest.fixture(scope="module")
def TSS_json_validator():
  validator = get_validator_for_program('TSS')
  return validator


@pytest.mark.parametrize("start_date, end_date, main_treatment_type"
                        , [('1/02/2019', '9/02/2020',  'assessment only')                                          
                          
                           ])
def test_too_long_assessment(TSS_json_validator, start_date, end_date, main_treatment_type):
   base1_error = copy.deepcopy(noerrors_base_translated)
   base1_error['main treatment type'] =  main_treatment_type
   base1_error['end date'] = end_date
   base1_error['commencement date'] = start_date

   errors, _ = TSS_json_validator.validate({'episodes' :[base1_error]})
   print(errors[0])
   assert errors[0] == [{ 
        'cid': '5119', 'etype': 'logic', 
        'field': 'end date', 'index': 0,
        'message': "For Main Treatment Type: 'Assessment' or 'Info/Education only', the episode duration must be less than 90 days."
      }]