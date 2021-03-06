from ..constants import MDS as M

rule_definitions = [
  {
    "message": f"AOD Counselling team only does the following treatment types: Counselling, Support and case management and Information and education",
    "field": M['MTT'],
    "type" : "Error",
    "rule": {"!":
              {"or" : [
                  {"==": [{"var": M['MTT']}, "rehabilitation"]},
                  {"==": [{"var": M['MTT']}, "withdrawal management (detoxification)"]},
                  {"==": [{"var": M['MTT']}, "pharmacotherapy"]},
              ]}
            }
  }
]