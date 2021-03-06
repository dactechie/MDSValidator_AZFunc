
# drugs = [
#   {
#     "id":1,
#     "name":"diazepam", # generic,
#     "codes": {"act": 232, "nsw":23},
#     "category": "sedative",  
#     "class": "benzodiazepines", # or "parent"
#     "aliases": ["valium"], # street names, commerical product names
#     "usage":	["ingests"],
#   }
   
# ]
drug_usage = {

"alcohols nfd"    : 	["ingests"],
"alcohol"         :   ["ingests",	"injects", "not stated/inadequately described", "smokes", "other"],
"alprazolam"      :   ["ingests"],
"amphetamines, n.e.c."  : 	["ingests",	"inhales (vapour)",	"injects",	"smokes"],
"analgesics"      :   ["ingests"],
"amphetamine"     : 	["ingests",	"inhales (vapour)",	"injects",	"smokes"],
"anabolic androgenic steroids nfd": ["injects"],

"benzodiazepines nfd": ["ingests"],
"benzodiazepines, n.e.c.": ["ingests", "injects",	"smokes", "sniffs (powder)" ],
"buprenorphine"   : 	["ingests", "smokes"],

"caffeine"        :   ["ingests"],
"cannabinoids"    : 	["ingests",	"inhales (vapour)",	"smokes"],
"cocaine"         : 	["ingests","sniffs (powder)", "injects"],
"codeine"         : 	["ingests"],

"dexamphetamine"  : 	["injects", "ingests"],
"diazepam"        : 	["ingests", "smokes", "sniffs (powder)"],
"fentanyl"        :   ["smokes", "injects", "ingests", "sniffs (powder)", "other"],

"ghb type drugs and analogues, n.e.c.": ["ingests", "inhales (vapour)"],
"heroin"          : 	["ingests",	"injects", "smokes", "inhales (vapour)", "not stated/inadequately described"],
"ketamine"        : 	["ingests", "sniffs (powder)"],

"methamphetamine" : 	["ingests",	"inhales (vapour)",	"injects",	"not stated/inadequately described", "smokes",	"sniffs (powder)"],
"methadone"       : 	["injects", "ingests", "smokes", "not stated/inadequately described"],
"mdma"            : 	["ingests","sniffs (powder)", "smokes"],
"mda"             : 	["ingests"],
"morphine": ["ingests", "injects", "smokes","not stated/inadequately described","inhales (vapour)"],

"nicotine": ["ingests",	"inhales (vapour)", "smokes"],
"not stated / inadequately described" : 	["injects", "ingests",	"not stated/inadequately described"],
"not stated/inadequately described" : ["not stated/inadequately described"],            # todo cleanup with the above

"opioid analgesics nfd" : ["ingests"],
"other antidepressants and antipsychotics, n.e.c.": ["ingests"],


"other drugs of concern" : 	["not stated/inadequately described", "sniffs (powder)"],
"oxycodone"              : 	["ingests"],
"quetiapine"             :  ["ingests"],
"testosterone"           :  ["injects"],
"tramadol"               : 	["ingests"],
"zolpidem"               : 	["ingests"]
}

drug_usage["analgesics nfd"] = drug_usage["analgesics"]
drug_usage["cannabinoid agonists"] = drug_usage["cannabinoids"]
drug_usage["cannabinoids and related drugs, n.e.c."] = drug_usage["cannabinoids"]
drug_usage["ghb type drugs and analogues nfd"] = drug_usage["ghb type drugs and analogues, n.e.c."]
drug_usage["opioid antagonists, n.e.c."] = drug_usage["opioid analgesics nfd"]