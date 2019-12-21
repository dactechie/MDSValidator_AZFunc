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
        "ID", "SLK 581",
        "Sex", "DOB", "Date accuracy indicator", "Country of birth",  "Postcode (Australian)",
        "Indigenous status", "Preferred language",
        "Commencement date", "End date","Client type",
        "Principle drug of concern", "ODC1", "ODC2", "ODC3","ODC4", "ODC5",
        "Main treatment type",       "OTT1", "OTT2", "OTT3","OTT4",
        "Reason for cessation",
        "Method of use for PDC","Usual accommodation", "Living arrangements",
        "Injecting drug use status", "Treatment delivery setting", "Source of referral", 
        "Mental health", "Previous alcohol and other drug treatment received"
      ],
      "anyOf" : [
        {"required" : ["First name","Surname"]},
        {"required" : ["FULL NAME"]}
      ],
      "properties": {
          "ENROLLING PROVIDER": { "type": "string", "description": "XXENROLPROVIDER"},
          "First name":  { "type": "string" , "description": "FNAME"} ,
          "Surname":  { "type": "string" , "description": "LNAME"},
          "FULL NAME":  { "type": "string" , "description": "XXFULLNAME"},
          "ID":   { "type": "string" },           
          "Sex":  { "type": "string", "description":"SEX", "enum": [ "Male", "Female", "Other", "Not stated"] },
          "DOB":  { "type": "string" },
          "Date accuracy indicator": {"enum": date_accuracy_indicator['enum'] , "description": "DAI"},
          "SLK 581":            {"type": "string", "description": "SLK",
           "slkpattern" : "^[2A-Z]{5}([012]?[0-9]|3[01])(0?[1-9]|1[012])(19[4-9][0-9]|20[01][0-9])[01]$"
          },
          "Country of birth":   {"enum": definition_countries['enum'] , "description": "COB"},
          "Indigenous status":  {"enum": ATSI['enum'] , "description": "ATSI"},
          "Preferred language": {"enum": definition_languages['enum'], "description": "PLANG"},
          "Postcode (Australian)": {"type": "string", "description": "PCODE",
            "pattern" : "^[0-9]{4}|Overseas|Other|No fixed address (or not applicable)|Unknown|Not stated/inadequately described$"
          },
          "Commencement date" : {"type": "string", "description": "COMM_DATE" },
          "End date": {"type": "string", "description": "END_DATE" },
          "Client type": {"type": "string", "description": "CLNT_TYP",
            "enum": ["Own alcohol or other drug use", "Other's alcohol or other drug use"]
          },
          "Principle drug of concern": {"enum": drugs['enum'], "description": "PDC"},
          "ODC1":{"enum": drugs['enum']}, "ODC2":{"enum": drugs['enum']}, "ODC3":{"enum": drugs['enum']},
          "ODC4":{"enum": drugs['enum']}, "ODC5":{"enum": drugs['enum']},

          "Main treatment type": {"enum": treatment_type['enum'],  "description": "MTT"},
          "OTT1": {"enum": other_treatment_type['enum']}, "OTT2": {"enum": other_treatment_type['enum']},
          "OTT3": {"enum": other_treatment_type['enum']}, "OTT4": {"enum": other_treatment_type['enum']},

          "Reason for cessation": {"enum": cessation_reason['enum'], "description": "REAS_CESS"},

          "Method of use for PDC" : {"type": "string",  "description": "METHOD",
            "enum": ["", "Ingests", "Smokes", "Injects", "Sniffs (powder)", "Inhales (vapour)", "Other",
              "Not stated/inadequately described"]
          },
          "Usual accommodation" :       {"enum" : accommodation['enum'], "description": "USACC"},
          "Living arrangements":        {"enum" : living_arrangements['enum'] , "description": "LIVAR"},
          "Injecting drug use status":  {"enum": injt_drug_use_status['enum'], "description": "INJ_USE"},
          "Treatment delivery setting": {"enum": treatment_delivery_setting['enum'], "description": "TDS"},
          "Source of referral":         {"enum": referral_source['enum'], "description": "SRC_REF"},
          "Mental health":              {"enum": mental_health['enum'], "description": "MENT_HEL"},
          "Previous alcohol and other drug treatment received": {"enum": previous_treatment_type['enum'], "description": "PREV_AOD"}
        }
      }
    }
}