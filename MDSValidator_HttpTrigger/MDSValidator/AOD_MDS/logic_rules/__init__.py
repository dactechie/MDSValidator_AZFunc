from  ..constants import program_domain_map             

def get_program_rules(program_name):
  domain = program_domain_map.get(program_name)
  if not domain:
    return None
    
  if domain == 'ACTMDS':
    from .ACTMDS import program_types
  else:
    from .NSWMDS import program_types

    
  return program_types.get(program_name)
  