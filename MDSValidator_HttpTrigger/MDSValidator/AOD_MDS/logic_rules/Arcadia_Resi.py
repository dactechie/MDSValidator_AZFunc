from ..constants import MDS as M

rule_definitions = [
  # Non-residential treatment types delivered in residential treatment facilities
  # Logic 24  
  # Warning
  # Records were found where Main treatment type was coded '5' (support and case management only), '6' (information and education only) or '7' (assessment only) and Treatment delivery setting was coded '2' (residential treatment facility).
  # This combination of responses may not be valid in all circumstances or may require further explanation. please review these records and amend any incorrect data.


  {
    "message": f"Arcadia-Resi program only does the following treatment types: Counselling, Support and case management, Rehab, Detox",
    "field": M['MTT'],
    "type" : "Error",
    "rule": {"!": 
              {"or" : [
                  {"==": [{"var": M['MTT']}, "Information and education"]},
                  {"==": [{"var": M['MTT']}, "Pharmacotherapy"]}                  
              ]}
            }
  },
  {
    "message": f"Arcadia-Resi program does not provide service (treatment delivery) in Home/'Other' settings.",
    "field": M['TDS'],
    "type" : "Error",
    "rule": {"!": 
              {"or" : [
                  {"==": [{"var": M['TDS']}, "Home"]},
                  {"==": [{"var": M['TDS']}, "Other"]}
              ]}
            }
  },
  {
    "message": f"If {M['TDS']} is Residential treatment', '{M['MTT']}' has to be Withdrawal Mgmt.(Detox) / Rehab.",
    "field": M['TDS'],
    "type" : "Error",
    "rule": {"if": [ 
              {"==": [{"var": M['TDS']}, "Residential treatment facility"]},
              {"in": [{"var":M['MTT']}, ["Rehabilitation","Withdrawal management (detoxification)"]]},
              True
            ]}
  },

  # TODO 
  # no outreach 
]
