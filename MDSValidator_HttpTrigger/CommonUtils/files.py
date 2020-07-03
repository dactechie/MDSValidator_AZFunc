
import json
from os import path

# folder_type : schema / logic_rules
def pather(folder_type, sub1, sub2):# sub1 :schema_domain, : schema-version
  basepath = path.dirname(__file__)
  filepath = path.abspath(path.join(basepath, "..",
                          f"MDSValidator/AOD_MDS/{sub1}/{sub2}/{folder_type}"))
  return filepath

def load_from_file(path_filename):
  obj = None
  with open(f"{path_filename}.json") as f:
    obj = json.load(f)

  return obj
