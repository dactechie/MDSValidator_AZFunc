from os import path
from .SchemaProvider import SchemaProvider
from ...CommonUtils.files import load_from_file \
          , pather # TODO: NOT WORKING .. 

# type : schema / logic rules
def _build_schema_path(schema_domain, schema_version):
  basepath = path.dirname(__file__)
  filepath = path.abspath(path.join(basepath, "..", "..", f"MDSValidator/AOD_MDS/schema"))
  
  return f"{filepath}/{schema_domain}/{schema_version}"



class FileSchemaProvider(SchemaProvider):

  def build_schema(self):    
    schema_path = _build_schema_path(self.schema_domain, self.schema_version)
    
    main_schema =  load_from_file(f"{schema_path}/schema")
    defs =  load_from_file(f"{schema_path}/definitions")

    for n in ("countries", "drugs", "languages"): # from local .json files
      defs["definitions"][n] =  load_from_file(f"{schema_path}/{n}")
    
    return main_schema, defs