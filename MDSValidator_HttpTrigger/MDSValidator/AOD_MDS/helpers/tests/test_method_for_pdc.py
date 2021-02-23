

import pytest
from . import method_of_use_matrix
from ..others import is_valid_drug_use

@pytest.mark.parametrize("drug, method ,expected", [
    ("cocaine", "ingests", True),  
    ("nicotine", "injects", False),
    ("nisdfsdcotine", "injects", False),
    ("cocaine", "indsfjects", False),
    ("analgesics nfd", "ingests", True),
    ("opioid antagonists, n.e.c.", "ingests", True), # translated opioid antagonists nfd
    ("opioid analgesics nfd", "ingests", True),
    ("mdma", "smokes", True),
    ("alprazolam", "ingests", True),
])
def test_usage_method(drug, method, expected):

  assert is_valid_drug_use(method_of_use_matrix.drug_usage, drug, method) == expected
