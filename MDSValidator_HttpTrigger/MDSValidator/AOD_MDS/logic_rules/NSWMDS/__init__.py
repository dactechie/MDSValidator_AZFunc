from ..counselling_info import rule_definitions as counselling_info
from .non_residential import rule_definitions as non_residential
from .cross_field_required import rule_definitions as xfield_rules
#from .residential import rule_definitions as residential

program_types = {
  'Pathways' : [*counselling_info, *non_residential, *xfield_rules],
}