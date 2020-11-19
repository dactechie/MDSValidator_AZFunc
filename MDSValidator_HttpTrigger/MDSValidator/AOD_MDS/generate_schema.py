import json
from csv import reader as csv_reader
from os import path
from glob import glob

# takes an input folder with csv files like : 
# Drugs.csv : 
#code,value
#0000,not stated/inadequately described
#1210,inadequately described

# generates .json files like these : (strips the code content)
#{
  # "type": "string",
  # "$id": "#drugs",
  # "enum": [
  #   "",
  #   "inadequately described",
  #   "not stated",
  #   "alcohol",


def get_enumkeys_obj(csv_file, data_type):
  newpyobj = {}
  with open(csv_file, mode="r", encoding='utf-8') as f:
    datareader = csv_reader(f)
    next(datareader) # skip header  
    newpyobj = {
      "type" : "string",
      "$id"  : f"#{data_type}",
      "enum" : [row[1] for row in datareader]
    }
  return newpyobj


def generate_schema_file(csv_filename, outfile_path):
  
  fname = path.basename(csv_filename)
  csv_filename_noext = str.lower(path.splitext(fname)[0])
  csv_filename_noext = csv_filename_noext.split("_")[0] # input csv files can have versions Languages_ASCL2016.csv
                                                        #  we don't need the _ASCL.. part
  full_outfilename = path.join(outfile_path, f"{csv_filename_noext}.json")

  with open(full_outfilename, mode="w", encoding='utf-8') as output_file:
    new_obj = get_enumkeys_obj(csv_filename, data_type=csv_filename_noext)
    print("writing to " + full_outfilename)
    json.dump(new_obj, output_file, ensure_ascii=False, indent=2)



def get_input_files(basepath, domain):
  list_of_files = glob(path.join(basepath, domain,'*.csv')) # * means all if need specific format then *.csv
  if not any(list_of_files):
    print("no input csv file in the input folder !")
    return None
  return list_of_files

basepath = path.dirname(__file__)
source_path = path.abspath(path.join(basepath, "schema_sources"))
domain = "ACT"
list_of_files = get_input_files(source_path, domain)
outfile_path = path.abspath(path.join(basepath, "generated_schemas", f"{domain}MDS"))

for src_fname in [lf for lf in list_of_files if lf is not "definitions.csv"] :
  generate_schema_file(src_fname, outfile_path)
