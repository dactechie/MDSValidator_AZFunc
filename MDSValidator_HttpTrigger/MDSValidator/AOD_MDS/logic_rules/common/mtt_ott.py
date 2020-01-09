from ...constants import MDS as M

rule_definitions = [

  # Incorrect additional treatment type
  # ValidationCode: Logic 10
  # Records were found where Main treatment type was '5' (Support and case management only), '6' (Information and education only) or 
  # '7' (Assessment only) and an additional treatment was recorded. 
  # Records where that Main treatment type specifies that it is the 'only' treatment cannot have additional treatment types.
  # {   # old rule  1 July 2018 onwards no "only"
  #   "message": "Incorrect additional treatment type (when MTT has the word 'only')",
  #   "field": M['MTT'],
  #   "type" : "Error",
  #   "rule": {"!":
  #       {"if": [
  #           {"==" : ["only", 
  #                         {"substr": [ {"var": M['MTT'] },-4] }
  #                   ] },
  #           {"!=":  [ {"cat": [
  #                       {"var":'OTT1'}, {"var":'OTT2'}, {"var":'OTT3'}, {"var":'OTT4'}
  #                       ]},
  #                   "" ]}
  #         ]
  #       }
  #     }
  # },

 {
      "message": "Can't have duplicate MTT/OTTs.",
      "field": 'ott4',
      "type" :"Error",
      "rule":{"!": 
          {"has_duplicate_values": [{"var": 'ott4'}, [{"var": 'ott1'}, {"var": 'ott2'},
                                    {"var": 'ott3'}, M['MTT']]]}
      }
  },
  {
      "message": "Can't have duplicate MTT/OTTs.",
      "field": 'ott3',
      "type" :"Error",
      "rule":{"!": 
          {"has_duplicate_values": [{"var": 'ott3'}, [{"var": 'ott1'}, {"var": 'ott2'}, M['MTT']]]}
      }
  },
  {
      "message": "Can't have duplicate MTT/OTTs.",
      "field": 'ott2',
      "type" :"Error",
      "rule":{"!": 
          {"has_duplicate_values": [{"var": 'ott2'}, [{"var": "ott1"}, M['MTT']]]}
      }
  },
  {
      "message": "Can't have duplicate MTT/OTTs.",
      "field": M['MTT'],
      "type" : "Error",
      "rule":{"!": 
          {"has_duplicate_values": [{"var":M['MTT']}, [{"var":"ott1"}]]}
      }
  },
]