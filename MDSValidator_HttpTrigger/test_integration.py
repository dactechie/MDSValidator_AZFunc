
import pytest
import datetime
#import json
import csv
import os
from .MDSValidator import MDSDataFileProcessor
from .input_file_processor import get_details_from

headerTSS= "enrolling provider,Client ID,Surname,First name,eid,Age,Sex,Date of birth,Country of birth,Indigenous status,Preferred language,Client type,\
  Source of referral,Commencement date,End date,Reason for cessation,Treatment delivery setting,Method of use for PDC,Injecting drug use status,PDC,\
    ODC1,ODC2,ODC3,ODC4,ODC5,Main treatment type,OTT1,OTT2,OTT3,OTT4,Date accuracy indicator,SLK 581,Postcode (Australian),Usual accommodation,\
      Living arrangements,Previous alcohol and other drug treatment received,Mental health"

dataTSS = "MJ JM,505,'UCHYT, CARIF',820002000,54,Male,7/12/1965,Sudan,Neither Aboriginal nor TSI,Arabic (Including Lebanese), \
Own alcohol or other drug use,Other community/health service,29/01/2020,1/7/2020,Treatment completed,Non-residential Facility,Ingests,\
Not stated / inadequately described,Opioid Antagonists nfd,,,,,,Assessment only,,,,,AAA,CHTAR071219651,2606,Private Residence,Alone, \
Not Stated / Inadequately Described,,,,Counselling and Case Management"
dataTSS = [headerTSS, dataTSS]

resultTSS = [{'enrolling provider': 'mj jm', 'error_enrolling provider': '', 'id': '505', 'error_id': '', 'first name': "carif'", 
'error_first name': '', 'surname': "'uchyt", 'error_surname': '', 'eid': '820002000', 'error_eid': '', 'slk 581': 'CHTAR071219651', 
'error_slk 581': '', 'sex': 'male', 'error_sex': '', 'dob': '07/12/1965', 'error_dob': '', 'date accuracy indicator': 'aaa - day, month and year are accurate',
 'error_date accuracy indicator': '', 'country of birth': 'sudan', 'error_country of birth': '', 'indigenous status': 'neither aboriginal nor torres strait islander origin',
 'error_indigenous status': '', 'preferred language': 'arabic (including lebanese)', 'error_preferred language': "invalid value/format: 'arabic (including lebanese)'",
  'postcode (australian)': '2606', 'error_postcode (australian)': '', 'usual accommodation': 'private residence', 'error_usual accommodation': '', 
  'client type': 'own alcohol or other drug use', 'error_client type': '', 'source of referral': 'other community/health care service', 'error_source of referral': '', 
  'commencement date': '29/01/2020', 'error_commencement date': '', 'end date': '01/7/2020', 'error_end date': 'Episode End Date is not in the reporting period',
   'reason for cessation': 'treatment completed', 'error_reason for cessation': '', 'treatment delivery setting': 'non-residential treatment facility', 
   'error_treatment delivery setting': '', 'method of use for pdc': 'ingests', 'error_method of use for pdc': '', 
   'injecting drug use status': 'not stated/inadequately described', 'error_injecting drug use status': '', 'principle drug of concern': 'opioid antagonists, n.e.c.', 
   'error_principle drug of concern': '', 'odc1': '', 'error_odc1': '', 'odc2': '', 'error_odc2': '', 'odc3': '', 'error_odc3': '', 'odc4': '', 'error_odc4': '',
    'odc5': '', 'error_odc5': '', 'main treatment type': 'assessment only', 'error_main treatment type': '', 'ott1': '', 'error_ott1': '', 'ott2': '', 'error_ott2': '',
     'ott3': '', 'error_ott3': '', 'ott4': '', 'error_ott4': '', 'living arrangements': 'alone', 'error_living arrangements': '', 
     'previous alcohol and other drug treatment received': 'not stated / inadequately described', 
    'error_previous alcohol and other drug treatment received': "invalid value/format: 'not stated / inadequately described'", 'mental health': '', 'error_mental health': ''}]


headerEuro = [
  #"Staff",  "PID","Last Name","First Name","SLK 581", "Sex","Date of birth","Date accuracy indicator (for DoB)", # TODO Add SLK to input data file
    "Staff", "Location", "Service", "PID","Last Name","First Name","SLK 581", "Sex","Date of birth","Date accuracy indicator (for DoB)", # TODO Add SLK to input data file
    "Country of birth","Indigenous status", "Preferred language","Postcode - Australian",
    "Usual accommodation","Client type",
    "Source of referral","Principal Source of Income","Commencement Date","End date","Reason for cessation",
    "Referral to Another Service","Treatment delivery setting",
    "Method of use for principal drug of concern","Injecting drug status","PDC","ODC1","ODC2","ODC3","ODC4","ODC5",
    "Main treatment type (MTT)","OTT1","OTT2","OTT3","OTT4","Living arrangements",
    "Previous AOD treatment","Mental health (Diagnosed with a mental illness)"
  ]
dataEuro = [
    "Aftab Jalal", "Eurobodalla", "Pathways", "59","May","James","OFIAT170719681","Male","17071968",
    'not estimated',"Australia", "Neither Aboriginal nor TSI","English","2536",
    "Privately owned house or flat","Own drug use",
    "Other hospital","Not stated/not known/inadequately described",
    "7122018","19022020","Left without notice","Not stated/inadequately described","Community/ Outpatient",
    "Ingest","Never injected","Alcohol","","","","","",
    "Support and case management only","","","","","Alone",
    "no previous service received","Not stated/inadequately described"
]

resultEuro = [{'staff': 'aftab jalal', 'error_staff': '', 'location': 'eurobodalla', 'error_location': '', 'service': 'pathways', 
'error_service': '', 'id': '59', 'error_id': '', 'first name': 'james', 'error_first name': '', 'surname': 'may', 'error_surname': '', 
'slk 581': 'OFIAT170719681', 'error_slk 581': 'AY2AM170719681', 'sex': 'male', 'error_sex': '', 'dob': '17071968', 'error_dob': '',
 'date accuracy indicator': 'not estimated',
  'error_date accuracy indicator': "", 
  'country of birth': 'australia', 'error_country of birth': '', 'indigenous status': 'neither aboriginal nor torres strait islander origin', 
  'error_indigenous status': '', 'preferred language': 'english', 'error_preferred language': '', 'postcode (australian)': '2536',
   'error_postcode (australian)': '', 'usual accommodation': 'privately owned house or flat', 'error_usual accommodation': '',
    'client type': 'own alcohol or other drug use', 'error_client type': '', 'source of referral': 'other hospital', 
    'error_source of referral': '', 'principal source of income': 'not stated/not known/inadequately described', 
    'error_principal source of income': '', 
    'commencement date': '07122018', 'error_commencement date': '', 
    'end date': '19022020', 'error_end date': '', 'reason for cessation': 'left without notice', 'error_reason for cessation': '',
     'referral to another service': 'not stated/inadequately described', 'error_referral to another service': '', 
     'treatment delivery setting': 'community/ outpatient', 'error_treatment delivery setting': '', 'method of use for pdc': 'ingests',
      'error_method of use for pdc': '', 'injecting drug use status': 'never injected', 'error_injecting drug use status': '', 
      'principle drug of concern': 'alcohol', 'error_principle drug of concern': '', 'odc1': '', 'error_odc1': '', 'odc2': '', 
      'error_odc2': '', 'odc3': '', 'error_odc3': '', 'odc4': '', 'error_odc4': '', 'odc5': '', 'error_odc5': '', 
      'main treatment type': 'support and case management only', 'error_main treatment type': '', 'ott1': '', 'error_ott1': '', 
      'ott2': '', 'error_ott2': '', 'ott3': '', 'error_ott3': '', 'ott4': '', 'error_ott4': '', 'living arrangements': 'alone',
       'error_living arrangements': '', 'previous alcohol and other drug treatment received': 'no previous service received', 
       'error_previous alcohol and other drug treatment received': '', 'mental health': 'not stated/inadequately described', 
       'error_mental health': ''}]
 

dataEuro = [",".join(headerEuro) , ",".join(dataEuro)]

# def load_params_from_json(json_path):
#     with open(json_path) as f:
#         return json.load(f)

@pytest.mark.parametrize( "data, result,open_and_closed_eps, errors_only, start_date, program, reporting_period", [
                        #  (dataTSS, resultTSS, True, False, datetime.datetime(2020,1,1), 'TSS', 6),
                          (dataEuro, resultEuro, True, False, datetime.datetime(2020,1,1), 'PathwaysEuroMonaBega', 6)
                        ])
def test_main(data, result, open_and_closed_eps, errors_only, start_date, 
                program, reporting_period):
    result_dicts = MDSDataFileProcessor.main(data, 
                      open_and_closed_eps, 
                      errors_only,
                      start_date, 
                      program,
                      reporting_period, 
                      nostrict=False)
        
    assert(result_dicts == result)



def write(data_dicts, outfile):  
  with open(outfile, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data_dicts[0].keys())

    writer.writeheader()
    for r in data_dicts:  
      writer.writerow(r)


def main_tester(lines, dirname, filename):
    # result_dicts = MDSDataFileProcessor.main(dataTSS, 
    #                   open_and_closed_eps=True, 
    #                   errors_only=False,
    #                   start_date=datetime.datetime(2020,1,1), 
    #                   program='TSS',
    #                   reporting_period=6, 
    #                   nostrict=False)    
    program, start_date, period = get_details_from(filename)

    result_dicts = MDSDataFileProcessor.main(lines,
                      open_and_closed_eps=True,
                      errors_only=False,
                      start_date=start_date,
                      program=program,
                      reporting_period=period,
                      nostrict=False)

    write(result_dicts, os.path.join(dirname, f'output_{filename}'))
    
    # print(result_dicts[0].keys())
    # print(result_dicts[0].values())


def load_file(dirname, filename):
  
  with open(os.path.join(dirname,  filename)) as f:
    return f.readlines()
  

def test_file():
  dirname = os.path.join(os.path.dirname(__file__), "test_integ_data")
  
  filename = "Althea_012020_12.csv" # "new_TSS_012020_6.csv"
  lines = load_file(dirname,filename)
  
  # print(lines)
  main_tester(lines, dirname, filename)


# TODO":  Addd JSON Logic: "Others drug use" : Previous AOD: Blank or "Not collected"

if __name__ == '__main__':
  #os.path.realpath(__file__)
  dirname= r"C:\Users\aftab.jalal\dev\MDSValidator_AZFunc\MDSValidator_HttpTrigger"
  dirname = os.path.join(dirname, "test_integ_data")
  #print(os.path.abspath(__file__))
  print(dirname)
  filename = "Test3_PathwaysEuroMonaBega_012020_6.csv" # "AMDS_PathwaysEuroMonaBega_072020_1.csv" #"FakeNames_PathwaysEuroMonaBega_012020_6.csv"
  lines = load_file(dirname,filename)
  
  # print(lines)
  main_tester(lines, dirname, filename)