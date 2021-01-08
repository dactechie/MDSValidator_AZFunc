from ..counselling_info import rule_definitions as counselling_info
from .non_residential import rule_definitions as non_residential
from .Arcadia_Resi import rule_definitions as residential
from .Althea import rule_definitions as althea_rules


program_types = {
  'Althea'      : althea_rules,
  'TSS'         : [*counselling_info, *non_residential],
  'ArcadiaDay'  : [*counselling_info, *non_residential],
  'ArcadiaResi' : [*residential],
  'Sapphire'    : [*counselling_info, *non_residential]
}