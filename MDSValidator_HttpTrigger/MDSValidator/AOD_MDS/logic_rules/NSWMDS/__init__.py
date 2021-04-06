from ..counselling_info import rule_definitions as counselling_info
from .non_residential import rule_definitions as non_residential
#from .residential import rule_definitions as residential

program_rules = {
  'PathwaysEuroMonaBega' : [*counselling_info, *non_residential],
  'Sapphire'             : [*counselling_info, *non_residential]
}