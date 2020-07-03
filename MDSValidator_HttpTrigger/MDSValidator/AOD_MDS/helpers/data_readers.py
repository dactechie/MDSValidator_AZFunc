
import copy
import csv
import json
from ...logger import logger
from ..constants import MDS
from ...utils import remove_unicode, get_lower_case_vals


# def cleanse_header(csvfile, data_header):
#   clean_header = True
#   if MDS['FNAME'] not in data_header and "FULL NAME" in data_header:
#     reader = csv.DictReader(csvfile, data_header)
#     #    rows = _split_fullname(reader)
#     #reader = rows
#     data_header.remove("FULL NAME")
#     data_header.extend([MDS['FNAME'], MDS['LNAME']])
  
#   result = {}
#   for dh in data_header:
#     tmp = remove_unicode(dh)    
#     if dh is not tmp:
#       clean_header = False    
#     result[dh] = tmp
#   return result, clean_header


def load_from_file(self, path_filename):
  obj = None
  with open(f"../schema/{path_filename}.json") as f:
    obj = json.load(f)

  return obj


def read_header(filename: str) -> list:
  with open(filename, 'r') as csvfile:
    headers = [header for header in csvfile.readline().split(',')]
    headers[-1] = headers[-1].strip('\n')
    #cleanse_header(csvfile, headers)
    return headers


def _split_fullname(reader) -> list:
  data_dicts = []
  for i, r in enumerate(reader):
    if  "".join(r.values()) == '':
        logger.error(f"\n\tFound Blank row at {i}. Quitting...")
        return None

    row = copy.deepcopy(r)
    if row.get("full name"):              
        row[MDS['LNAME']], row[MDS['FNAME']]  = str.split(row["full name"], ", ")
        del row["full name"]
    
    data_dicts.append(row)

  return data_dicts


def get_dicts(data, header):
  results = []
  for d in data:
    results.append(
      {h: d[idxh] for idxh, h in enumerate(header)} )
  
  return results



# TODO clean this up (use a generator)
def read_data(data, data_header: dict, open_and_closed_eps=True) -> dict:
    """
    - Assumes that if a "FULL NAME" column exists, all rows will have a format of
        'LastName, FirstName'.
    - all_eps == False => Closed eps only
    """        
    data_dicts = get_dicts(data, data_header)

    if MDS['FNAME'] not in data_header and "full name" in data_header:
      data_dicts = _split_fullname(data_dicts)

    data_dicts = get_lower_case_vals(data_dicts, exception_fields=[ MDS['SLK'] ] )

    result = data_dicts
    if not open_and_closed_eps:         # has to have an end date, otherwise skip row
      result = [row for row in data_dicts if row[MDS['END_DATE']]]

    return { "episodes" :result }
