from ...constants import MDS as M

rule_definitions =[
 {
    "message": f"{M['END_DATE']} and {M['REF_ANO']} should be present together",
    "field": M['REF_ANO'],
    "type" : "Error",
    "rule":  {      
              "or":[
                  {"and": [
                      {"!=": [{"var": M['END_DATE']}, ""]},
                      {"!=": [{"var": M['REF_ANO']}, "" ]}
                  ]},
                  {"and": [
                      {"==": [{"var": M['END_DATE']}, ""]},
                      {"==": [{"var": M['REF_ANO']}, "" ]}
                  ]}
              ]
          }
  }

]