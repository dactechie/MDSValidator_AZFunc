from .accommodation import schema as accommodation
from .ATSI import schema as ATSI
from .cessation_reason import schema as cessation_reason
from .date_accuracy_indicator import schema as date_accuracy_indicator
from .definition_countries import schema as definition_countries
from .definition_languages import schema as definition_languages
from .drugs import schema as drugs
from .injt_drug_use_status import schema as injt_drug_use_status
from .living_arrangements import schema as living_arrangements
from .main_treatment_type import schema as treatment_type
from .other_treatment_type import schema as other_treatment_type
from .mental_health import schema as mental_health
from .previous_treatment_type import schema as previous_treatment_type
from .referral_source import schema as referral_source
from .treatment_delivery_setting import schema as treatment_delivery_setting

schema = {
  "type": "object",
  "version": 1.0,
  "description": " removed additionalProperties: false",
  "required": [ "episodes" ],
  "properties": {
    "episodes": {"type": "array", "items": { "$ref": "#/definitions/episode" } }
  },
  "definitions": {
    "episode": {
      "type": "object",
      "required": [
        "id", "slk 581",
        "sex", "dob", "date accuracy indicator", "country of birth",  "postcode (australian)",
        "indigenous status", "preferred language",
        "commencement date", "end date","client type",
        "principle drug of concern", "odc1", "odc2", "odc3","odc4", "odc5",
        "main treatment type",       "ott1", "ott2", "ott3","ott4",
        "reason for cessation",
        "method of use for pdc","usual accommodation", "living arrangements",
        "injecting drug use status", "treatment delivery setting", "source of referral", 
        "mental health", "previous alcohol and other drug treatment received"
      ],
      "anyOf" : [
        {"required" : ["first name","surname"]},
        {"required" : ["full name"]}
      ],
      "properties": {
          #"ENROLLING PROVIDER": { "type": "string", "description": "XXENROLPROVIDER"},
          "first name":  { "type": "string" , "description": "FNAME"} ,
          "surname":  { "type": "string" , "description": "LNAME"},
          "full name":  { "type": "string" , "description": "XXFULLNAME"},
          "id":   { "type": "string" },           
          "sex":  { "type": "string", "description":"SEX", "enum": [ "male", "female", "other", "not stated"] },
          "dob":  { "type": "string" },
          "date accuracy indicator": {"enum": date_accuracy_indicator['enum'] , "description": "DAI"},
          "slk 581":            {"type": "string", "description": "SLK",
           "slkpattern" : "^[2A-Z]{5}([012]?[0-9]|3[01])(0?[1-9]|1[012])(19[4-9][0-9]|20[01][0-9])[01]$"
          },
          "country of birth":   {"enum": definition_countries['enum'] , "description": "COB"},
          "indigenous status":  {"enum": ATSI['enum'] , "description": "ATSI"},
          "preferred language": {"enum": definition_languages['enum'], "description": "PLANG"},
          "postcode (australian)": {"type": "string", "description": "PCODE",
            "pattern" : "^[0-9]{4}|overseas|other|no fixed address (or not applicable)|unknown|not stated/inadequately described$"
          },
          "commencement date" : {"type": "string", "description": "COMM_DATE" },
          "end date": {"type": "string", "description": "END_DATE" },
          "client type": {"type": "string", "description": "CLNT_TYP",
            "enum": ["own alcohol or other drug use", "other's alcohol or other drug use"]
          },
          "principle drug of concern": {"enum": drugs['enum'], "description": "PDC"},
          "odc1":{"enum": drugs['enum']}, "odc2":{"enum": drugs['enum']}, "odc3":{"enum": drugs['enum']},
          "odc4":{"enum": drugs['enum']}, "odc5":{"enum": drugs['enum']},

          "main treatment type": {"enum": treatment_type['enum'],  "description": "MTT"},
          "ott1": {"enum": other_treatment_type['enum']}, "ott2": {"enum": other_treatment_type['enum']},
          "ott3": {"enum": other_treatment_type['enum']}, "ott4": {"enum": other_treatment_type['enum']},

          "reason for cessation": {"enum": cessation_reason['enum'], "description": "REAS_CESS"},

          "method of use for pdc" : {"type": "string",  "description": "METHOD",
            "enum": ["", "ingests", "smokes", "injects", "sniffs (powder)", "inhales (vapour)", "other",
              "not stated/inadequately described"]
          },
          "usual accommodation" :       {"enum" : accommodation['enum'], "description": "USACC"},
          "living arrangements":        {"enum" : living_arrangements['enum'] , "description": "LIVAR"},
          "injecting drug use status":  {"enum": injt_drug_use_status['enum'], "description": "INJ_USE"},
          "treatment delivery setting": {"enum": treatment_delivery_setting['enum'], "description": "TDS"},
          "source of referral":         {"enum": referral_source['enum'], "description": "SRC_REF"},
          "mental health":              {"enum": mental_health['enum'], "description": "MENT_HEL"},
          "previous alcohol and other drug treatment received": {"enum": previous_treatment_type['enum'], "description": "PREV_AOD"}
        }
      }
    }
}