from ...constants import MDS as M

rule_definitions =[
  {
    "message": f"{M['END_DATE']} and {M['REAS_CESS']} should be present together",
    "field": M['REAS_CESS'],
    "type" : "Error",
    "rule":  {      
              "or":[
                  {"and": [
                      {"!=": [{"var": M['END_DATE']}, ""]},
                      {"!=": [{"var": M['REAS_CESS']}, "" ]}
                  ]},
                  {"and": [
                      {"==": [{"var": M['END_DATE']}, ""]},
                      {"==": [{"var": M['REAS_CESS']}, "" ]}
                  ]}
              ]
          }
      
  }
]