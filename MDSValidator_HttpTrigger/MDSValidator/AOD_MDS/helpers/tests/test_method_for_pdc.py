

import pytest
from  MDSValidator.AOD_MDS.helpers.others import is_valid_drug_use


@pytest.mark.parametrize("drug, method ,expected", [
    ("cocaine", "ingests", True),  
    ("nicotine", "injects", False),
    ("nisdfsdcotine", "injects", False),
    ("cocaine", "indsfjects", False),
])
def test_usage_method(drug, method, expected):
  assert is_valid_drug_use(drug, method) == expected
