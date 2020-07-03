from ...constants import MDS as M

rule_definitions =[
  {
    "message": f"If {M['END_DATE']} is blank, {M['REAS_CESS']} should not be present",
    "field": M['REAS_CESS'],
    "type" : "Error",
    "rule":  {"and": [
                {"==": [{"var": M['END_DATE']}, ""]},
                {"==": [{"var": M['REAS_CESS']}, "" ]}                
            ]}
  },
  {
    "message": f"If {M['END_DATE']} is blank, {M['REF_ANO']} should not be present",
    "field": M['REF_ANO'],
    "type" : "Error",
    "rule":  {"and": [
                {"==": [{"var": M['END_DATE']}, ""]},
                {"==": [{"var": M['REF_ANO']}, "" ]}                
            ]}
  }
]