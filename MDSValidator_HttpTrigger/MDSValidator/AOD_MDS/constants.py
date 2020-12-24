
# schemaObj['definitions']['episode']['properties']['Principle drug of concern']['description']

# TODO: Build this from the schema.json file. The "description" for each property is the key and the 
# key of each property (in schema.json), is the value in the below dict.
MDS = {
    "ID": "id",
    "SEX": "sex",
    "COMM_DATE" : "commencement date",
    "DOB" : 'dob', #date of birth",
    "SLK": "slk 581",
    "FNAME": "first name",
    "LNAME": "surname",
    "DAI": "date accuracy indicator",
    "END_DATE" : "end date",
    "METHOD" : "method of use for pdc",
    "PDC" : "principle drug of concern",
    "INJ_USE" : "injecting drug use status",
    "CLNT_TYP" : "client type",
    "COB": "country of birth",
    "ATSI": "indigenous status",
    "PLANG": "preferred language",
    "PCODE": "postcode (australian)",
    "MTT": "main treatment type",
    "LIVAR": "living arrangements",
    "USACC": "usual accommodation",
    "TDS": "treatment delivery setting",
    "SRC_REF": "source of referral",
    "MENT_HEL": "mental health",
    "PREV_AOD": "previous alcohol and other drug treatment received", #previous aod treatment",
    "REAS_CESS": "reason for cessation",
    "SRC_INC": "principal source of income",
    "REF_ANO" :"referral to another service"
}

MDS_Dates = ("DOB", "COMM_DATE", "END_DATE")

MDS_ST_FLD = 'O'+MDS['COMM_DATE']
MDS_END_FLD = 'O'+MDS['END_DATE']

program_domain_map = {
  'TSS'         : 'ACTMDS',
  'Althea'      : 'ACTMDS',
  'ArcadiaResi' : 'ACTMDS',
  'ArcadiaDay'  : 'ACTMDS',

  'PathwaysEuroMonaBega' : 'NSWMDS',
  'Sapphire': 'NSWMDS'
}