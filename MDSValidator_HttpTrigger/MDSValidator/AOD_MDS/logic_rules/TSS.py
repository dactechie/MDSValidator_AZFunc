from ..constants import MDS as M

rule_definitions = [
  {
    "message": f"TSS team only does the following treatment types: Counselling, Support and case management and Information and education",
    "field": M['MTT'],
    "type" : "Error",
    "rule": {"!": 
              {"or" : [
                  {"==": [{"var": M['MTT']}, "Rehabilitation"]},
                  {"==": [{"var": M['MTT']}, "Withdrawal management (detoxification)"]},
                  {"==": [{"var": M['MTT']}, "Pharmacotherapy"]},
              ]}
            }
  },
  {
    "message": f"TSS team does not provide service (treatment delivery) in Home/'Other'/Resi setting ",
    "field": M['TDS'],
    "type" : "Error",
    "rule": {"!": 
              {"or" : [
                  {"==": [{"var": M['TDS']}, "Home"]},
                  {"==": [{"var": M['TDS']}, "Other"]},
                  {"==": [{"var": M['TDS']}, "Residential treatment facility"]},
              ]}
            }
  },
]
