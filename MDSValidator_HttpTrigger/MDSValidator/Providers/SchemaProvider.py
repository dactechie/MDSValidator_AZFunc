
from ..AOD_MDS.constants import program_domain_map

def _get_version_from_periodstart(period_start):
  return "07_2019" #f"v{period_start}"
  

class SchemaProvider:

  def __init__(self, period_start, program):
    self.schema_version = _get_version_from_periodstart(period_start)
    self.schema_domain = program_domain_map[program]

  def build_schema(self):
    pass




