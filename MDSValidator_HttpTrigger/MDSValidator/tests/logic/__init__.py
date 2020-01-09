
from collections import OrderedDict
from datetime import datetime as dt
from ...utils.dates import Period, get_period
from ...rule_checker.JSONValidator import JSONValidator
from ...AOD_MDS.constants import MDS as M

S_PRISON_OUTR = f"If {M['USACC']} is 'Prison/remand centre/youth training centre', '{M['TDS']}' has to be 'Outreach setting'."

period = get_period(start_date=dt(2018, 7, 1),period_months=12)


noerrors_base = OrderedDict(
  {
    "pat id": "5119","first name": "nick","surname": "adamopoulos","slk581": "daoic130819851","dob": "13/08/1985",
    "sex": "male","dob accuracy": "aaa","country": "australia","indig status": "neither aboriginal nor tsi","language": "english",
    "client": "own alcohol or other drug use","source": "correctional service","enrolment": "9/04/2018","discharge": "9/12/2018",
    "cessation": "","setting": "non-residential facility","use": "smokes","injection": "never injected",
    "drug": "nicotine","odc1": "","odc2": "","odc3": "","odc4": "","odc5": "","treat": "counselling","ott1": "",
    "ott2": "","ott3": "","ott4": "","postcode": "2913","living": "not stated / inadequately described","accom": "not stated/inadequately described",
    "previous treatment": "","mental health": "never been diagnosed"
  }
)


noerrors_base_translated = OrderedDict(
  {
    "id": "5119","first name": "nick","surname": "adamopoulos","slk 581": "DAOIC130819851","dob": "13/08/1985",
    "sex": "male",'date accuracy indicator': "aaa",  'country of birth': "australia", 'indigenous status': "neither aboriginal nor tsi", 'preferred language': "english",
    'client type': "own alcohol or other drug use", 'source of referral': "correctional service", 'commencement date': "9/04/2018", 'end date': "9/12/2018",
    'reason for cessation': "", 'treatment delivery setting': "non-residential facility", 'method of use for pdc': "smokes",  'injecting drug use status': "never injected",
    'principle drug of concern': "nicotine","odc1": "","odc2": "","odc3": "","odc4": "","odc5": "",'main treatment type': "counselling","ott1": "",
    "ott2": "","ott3": "","ott4": "", 'postcode (australian)': "2913", 'living arrangements': "not stated / inadequately described", 'usual accommodation': "not stated/inadequately described",
   'previous alcohol and other drug treatment received': "", 'mental health': "never been diagnosed"
  }
)

# PAT ID	First name	Surname	SLK581	DOB	SEX	DOB ACCURACY	COUNTRY	INDIG STATUS	
# LANGUAGE	CLIENT	SOURCE	ENROLMENT	DISCHARGE	CESSATION	SETTING	USE	INJECTION	DRUG	ODC1	ODC2	ODC3	ODC4	ODC5	
# TREAT	OTT1	OTT2	OTT3	OTT4	POSTCODE	LIVING	ACCOM	PREVIOUS TREATMENT	MENTAL HEALTH

#'ENROLLING PROVIDER': 'Tim Ireson' , 'ID':'11525','FULL NAME':'SILBY, JAYDEN','EID':'820002000','SLK581':'ILYAY111219961',
            #         'DOB':'3052010','SEX':'Male','AGE':'22',
            #         'Date accuracy indicator': 'AAA - Day, month and year are accurate', 'Country of birth': 'Australia',
            #         'Indigenous status': 'Neither Aboriginal nor Torres Strait Islander origin',
            #         'Preferred language': 'English', 'Client type': 'Own alcohol or other drug use', 'Source of referral':'Self', 'Commencement date': '4022019',
            #         'End date': '', 'DAYS ENROLLED': '', 'Reason for cessation': '', 'Treatment delivery setting': 'Non-residential treatment facility',
            #         'Method of use for PDC': 'Sniffs (powder)', 'Injecting drug use status': 'Never injected', 'Principle drug of concern': 'Diazepam',
            #         'ODC1': '', 'ODC2': '', 'ODC3': '', 'ODC4': '', 'ODC5': '', 'Main treatment type': 'Counselling', 'OTT1': '', 'OTT2': '', 'OTT3': '',
            #         'OTT4': '', 'Postcode (Australian)': '2906', 'Living arrangements': 'Alone', 'Usual accommodation': 'Private residence',
            #         'Previous alcohol and other drug treatment received': 'No previous treatment received', 'Mental health': 'Never been diagnosed', 'DIAGNOSIS': '', 'ARCADIA': '',
            #         'TREATED IN': '', 'PROGRAM': 'Counselling and Case Management', 'Surname': 'SILBY', 'First name': 'JAYDEN'}