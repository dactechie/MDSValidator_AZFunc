
from os import path
from glob import glob
from csv import reader as csv_reader
# from pprint import pprint
# from ..AOD_MDS.constants import MDS as M

# ArcadiaDay_072019_6.csv
# Enrolling Provider,EID,clientID,First Name,Surname,SLK 581,Sex,Date of birth,Date accuracy indicator (for DoB),Country of birth,Indigenous status,Preferred language,Postcode - Australian,Usual accommodation type,Client type,Source of referral,Commencement Date,End date,Reason for cessation,Treatment delivery setting,Method of use for principal drug of concern,Injecting drug status,PDC,ODC1,ODC2,ODC3,ODC4,ODC5,Main treatment type (MTT),OTT1,OTT2,OTT3,OTT4,Living arrangements,Mental health (Diagnosed with a mental illness),Previous AOD treatment
# dsg,dfg,1051,Aimee,Zardo,AROIM200119672,Female,20011967,"AAA - Day, month and year are accurate",Australia,Neither Aboriginal nor TSI,English,2603,Private residence,Own drug use,Self,29052019,15072019,Ceased to participate involuntary (non-compliance),Non-residential treatment facility,Ingests,Never injected,Alcohol,,,,,,Rehabilitation,,,,,Alone,Diagnosed more than twelve months ago,Rehabilitation
# dsg,dfg,7120,Rhys ,Sullivan,ULIHY131219951,Male,13121995,"AAA - Day, month and year are accurate",Australia,Neither Aboriginal nor TSI,English,2903,Private residence,Own drug use,Correctional Service,1072019,1102019,Treatment completed,Non-residential treatment facility,Smokes,Never injected,Methamphetamine,Cocaine,,,,,Rehabilitation,,,,,Spouse/partner and child(ren),Never been diagnosed,Rehabilitation
# dsg,dfg,10754,Robert,Howe,OW20B230419851,Male,23041985,"AAA - Day, month and year are accurate",Australia,Neither Aboriginal nor TSI,English,2913,Private residence,Own drug use,Self,14062019,11072019,Ceased to participate involuntary (non-compliance),Non-residential treatment facility,Ingests,Never injected,Alcohol,,,,,,Rehabilitation,,,,,Alone,Never been diagnosed,Rehabilitation

# translate headers
## open schema.json and pick all the $ref's
## open those csv files 

# EID,Person identifier,Sex,DOB,Country of birth,Indigenous status,Preferred language,Client type,Source of referral,Date of commencement of treatment episode for alcohol and other drugs,Date of cessation of treatment episode for alcohol and other drugs,Reason for cessation,Treatment delivery setting,Method of use for PDC,Injecting drug use status,Principal drug of concern,ODC1,ODC2,ODC3,ODC4,ODC5,Main treatment type,OTT1,OTT2,OTT3,OTT4,Date accuracy indicator,SLK 581,Postcode (Australian),Usual accommodation,Living arrangements,Previous AOD treatment,Mental health (Diagnosed with a mental illness),Medicine received alongside the main treatment type - opioid overdose reversal,Medicine received alongside the main treatment type - nicitone replacement therapy,Medicine received alongside the main treatment type - hepatitis C treatment
# 82A000002,10,1,21041971,1101,4,1201,1,1,4072019,4072019,1,4,1,4,2101,,,,,,6,,,,,AAA,ELKOH210419711,2612,11,1,1,9,,,
# 82A000002,10,1,21041971,1101,4,1201,1,1,10102019,28112019,1,4,1,4,2101,,,,,,5,,,,,AAA,ELKOH210419711,2612,11,1,1,9,,,
# 82A000002,44,1,20081984,1101,4,1201,1,1,23072019,23072019,1,1,3,1,3103,,,,,,6,,,,,AAA,AHAOU200819841,2606,11,5,2,9,,,
# 82A000002,56,2,21011975,1101,4,1201,1,1,16072019,16112019,1,1,1,4,9299,,,,,,5,,,,,AAA,OSEYP210119752,2617,11,2,5,9,,,
# 82A000002,56,2,21011975,1101,4,1201,1,1,25032020,28042020,1,1,2,4,7101,,,,,,5,,,,,AAA,OSEYP210119752,2617,11,2,2,9,,,
# 82A000002,213,1,11011977,1101,4,1201,1,2,27022020,27022020,1,4,1,4,2101,,,,,,6,,,,,AAA,RQEIG110119771,2602,11,1,99,9,,,
# 82A000002,366,1,30091976,1101,4,1201,1,1,10022020,10022020,1,1,3,3,3103,,,,,,6,,,,,AAA,ANAHR300919761,2612,11,1,5,9,,,

# basepath : schema_sources
# domain : ACT
# version_String 07_2019
def get_input_files(basepath, domain, version_string, subfolder):
  list_of_files = glob(path.join(basepath, domain, version_string, subfolder, '*.csv')) # * means all if need specific format then *.csv
  if not any(list_of_files):
    print("no input csv file in the input folder !")
    return None
  return list_of_files


# lookup csv
# AOD_MDS/schema_sources/ACT/07_2019/Definitions
# dict : {
#   cessation_reason : {
#     "Treatment Completed": 1

#   },
#   client_type : {
#     "own"  : 1,
#     "other": 2
#   } 
# }                
def read_csv_file_todict(csv_file):
  newpyobj = {}
  with open(csv_file, mode="r", encoding='utf-8') as f:
    datareader = csv_reader(f)
    next(datareader) # skip header  
    newpyobj = {str.lower(row[1]):row[0] for row in datareader} #row[0]: code
  return newpyobj

def get_def_type_from_filename(fullfilename):
  fname_with_ext = path.basename(fullfilename)
  csv_filename_noext = str.lower(path.splitext(fname_with_ext)[0])
  return csv_filename_noext

def build_definitions(domain, version_string):
  basepath = path.dirname(__file__)
  source_path = path.abspath(path.join(basepath, "schema_sources"))
  
  list_of_files = get_input_files(source_path, domain, version_string, "definitions")

  result = {}
  for file in list_of_files:
    csv_filename_noext = get_def_type_from_filename(file)
    result[csv_filename_noext] = read_csv_file_todict(file)
  return result


# domain = "ACT"
# version = "07_2019"
# result = build_definitions(domain, version)
# pprint(result)