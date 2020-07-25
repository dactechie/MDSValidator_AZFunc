from ..counselling_info import rule_definitions as counselling_info
from .non_residential import rule_definitions as non_residential
from .residential import rule_definitions as residential

program_types = {

  'TSS'         : [*counselling_info, *non_residential],
  'ArcadiaDay'  : [*counselling_info, *non_residential],
  'ArcadiaResi' : [*residential],
}