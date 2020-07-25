from  ...constants import MDS as M

rule_definitions = [
  {
    "message": f"Non-Residential team does not provide service (treatment delivery) in Home/'Other'/Resi setting ",
    "field": M['TDS'],
    "type" : "Error",
    "rule": {"!": 
              {"or" : [
                  {"==": [{"var": M['TDS']}, "home"]},
                  {"==": [{"var": M['TDS']}, "other"]},
                  {"==": [{"var": M['TDS']}, "residential treatment facility"]},
              ]}
            }
  },
]
