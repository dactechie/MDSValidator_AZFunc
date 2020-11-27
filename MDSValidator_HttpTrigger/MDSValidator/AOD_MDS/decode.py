from pprint import pprint
from .build_definitions_dictionary import build_definitions

from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.helpers.translators import (fields_map, headers_map, 
            translate_to_MDS_header, translate_to_MDS_values)

# domain = "ACT"
# version = "07_2019"
# result = build_definitions(domain, version)
# pprint(result)


#  ["id", "surname", "first name", "slk 581", "sex",	'dob', "date accuracy indicator", "country of birth", "indigenous status",
#                               "preferred language", "postcode (australian)",
#                               "usual accommodation",	"client type", "source of referral", "principal source of income","commencement date",
#                               "end date",	"reason for cessation", "referral to another service" , "treatment delivery setting", "method of use for pdc",
#                               "injecting drug use status", "principle drug of concern",	"main treatment type",	"living arrangements",	
#                               "previous alcohol and other drug treatment received", "mental health"] 

#     translate_to_MDS_header