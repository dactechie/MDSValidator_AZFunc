from .constants import MDS as M

mds_aliases = {
    # k (official name) : v [] -> array of aliases or accepted values

    "fields":{
        M['ATSI']: {        
          "neither aboriginal nor torres strait islander origin": ["neither aboriginal nor tsi", "not indigenous"],
          "aboriginal but not torres strait islander origin": ["aboriginal but not tsi", "aboriginal"],
          "torres strait islander but not aboriginal origin": ["tsi but not aboriginal"],
          "both aboriginal and torres strait islander origin": ["both aboriginal and tsi"],
        },
        M['COB']: {
          "vietnam" : ["viet nam"],
          "serbia" : ["serbia and montenegro"],
          "arabic" : ["arabic (including lebanese)"],
          "british antarctic territory" : ["british antarctic"],
          "myanmar" : ["burma (myanmar)", "burma (republic of the union of myanmar)"],
          "england" : ["united kingdom"],
        },        
        M['CLNT_TYP']:{
          "own alcohol or other drug use": ["own drug use", "own alcohol or other drug  use" ],
          "other's alcohol or other drug use": ["other's drug use", "other's alcohol/other drug use"],        
        },
        M['DAI']: {
          "aaa - day, month and year are accurate":[ "aaa" ],
          "eee - day, month and year are estimated":[ "eee" ],
          "uue - day and month are unknown, year is estimated": ["uue"],
          "uuu - day, month and year are unknown":      ["uuu"],        
          "eea - day and month are estimated, year is accurate" : ["eea"],
        },
        M['INJ_USE'] : {
          "not stated/inadequately described" : ["not stated / inadequately described"],
          "last injected more than twelve months ago":[
              "injecting drug use more than 12 months ago",
              "injecting drug use more than twelve months ago (and not in last twelve months)"],
          "last injected three months ago or less": [
              "current injecting drug use (last injectected prev 3 months)",
              "current injecting drug use (last injected within the previous three months)"],
          "last injected more than three months ago but less than or equal to twelve months ago": [ 
              "injecting drug use between 3 to 12 months ago",
              "injecting drug use more than three months ago but less than twelve months ago"]
        },
        M['LIVAR']: {          
          "friend(s)/parent(s)/relative(s) and child(ren)":
                  ["friend(s)/parent(s)/relative(s) and chil(ren)"],
          "spouse/partner and child(ren)" : ["spouse/partner and child(ren)"], 
          "alone" : ["alone"],
          "other relative(s)" : ["other relative(s)"], # TODO check me family memner/friend eqiuivalemtr
          "not known/inadequately described": ["not stated / inadequately described"]
        },        
        M['MENT_HEL']: {
          "not stated/inadequately described" : ["not stated / inadequately described" ],
          "diagnosed more than twelve months ago": ["diagnosed more than 12 months ago"],        
          "diagnosed three months ago or less" : ["diagnosed 3 months ago or less"],        
          "never been diagnosed": [ "not diagnosed, displaying possible symptoms"],
          "diagnosed more than three months ago but less than or equal to twelve months ago": [
            "diagnosed between 3 months and 12 months ago",
            "diagnosed more than three months ago or less than or equal to twelve month ago"
          ],
        },
        M['METHOD'] :{
          "not stated/inadequately described" : ["not stated"],
          # TODO : Hack - changed the NSW schema to take ingests instead of ingest
          # because after the aliasing to ingests is when the NSW schema validation occurs
          # and would be an error at that point 
          "ingests" : ["ingest"],
          "smokes"  : ["smoke"],
          "injects" : ["inject"],
          "sniffs (powder)": ["sniff (powder)"] ,
          "inhales (vapour)": ["inhale (vapour)"],
        },        
        M['MTT'] : {
          "counselling" : [ "dats counselling" ],
          "support and case management": ["support & case management only"],
        #  "Support and case management": ["Support and case management only", "Support & case management only"],
        #  "Information and education" : [ "Information and education only"],
         # "Assessment": ["Assessment only"]
        },
        M["PDC"]: {
              "not stated/inadequately described" :["not stated / inadequately described"],
              "heroin": ["heroin"],
              "opioid antagonists, n.e.c." : ["opioid antagonists, nec", "opioid antagonists nfd"],
              "methamphetamine" : ["crystal(meth) / ice / methamphetamine /speed",# coordinare sep 2019 ; mj's common drugs translation
                                   "ice"],   
              "lysergic acid diethylamide": ["lsd"],
              "alcohol": ["alcohol", "ethanol", "alcohol /ethanol"],
              "mdma": ["ecstasy (mdma)"],
              "cannabinoids" : ["cannabis", "cannabinoids and related drugs nfd", "cannabinoids (cannabis)"],
              "nicotine" : ["nicotine/tobacco"],
              "amphetamines nfd" : [ "amphetamines", "amphetamines, nfd" ],
              "benzodiazepines nfd" : ["benzodiazepines"],
              "analgesics nfd" : ["other analgesics"],
              "stimulants and hallucinogens nfd" : [ "other stimulants/hallucinogens"],
              "sedatives and hypnotics nfd": ["other sedatives/hypnotics"],
              "ghb type drugs and analogues, n.e.c." :["ghb type drugs and analogues nfd", "ghb type drugs and analogues, nec"],
        },
        M['REAS_CESS']: {
          "treatment completed" : ["treatment completed", "episode resolved"],
          "ceased to participate at expiation": ["ceased at expiation"],
          #['Treatment Resistance'],
          
          "ceased to participate against advice": ["ceased against advice"],
          "ceased to participate without notice" : ["ceased without notice"],
          "ceased to participate by mutual agreement": ["ceased by mutual agreement"],
          "ceased to participate involuntary (non-compliance)": ["ceased involuntary"],
          "change in main treatment type" : ["change in the main treatment type"],
          "change in principal drug of concern" : ["change in the principal drug of concern"],
          "change in delivery setting" : ["change in the delivery setting"],
          "transferred to another service provider" : ["transferred to other provider"],
          "imprisoned, other than drug court sanctioned":["imprisoned (not drug court)" ],
          "other" : ["other reason for cessation"]
        },
        M['PREV_AOD']:{          
          "withdrawal management (detoxification)":
              ["withdrawal management (detoxification)", "withdrawl management (detoxification)"],     
          "residential treatment facility" : ["residential treatment facility"],
          "no previous treatment received" : ["no treatment"]          
        },
        M['SRC_REF']:{
          "medical practitioner": ["medical practitioner"],
          "correctional service" : ["correctional service"],
          "family member/friend" : ["family member/friend"],
          "alcohol and other drug treatment service": ["alcohol & other drug treatment"],
          "other community/health care service" : ["other community/health service"]
        },
        M['TDS']:{
          "outreach setting" : ["outreach setting"],
          "private residence" : ["private residence", "rented private house or flat",
                                 "rented public house or flat"],
          "non-residential treatment facility" :["non-residential facility"]
        },
        M['USACC']:{
          "private residence": ["rented public house or flat", 
                                "rented private house or flat"],
          "alcohol and other drugs": ["alcohol/other drug treatment residence"],
          "short term crisis, emergency or transitional accommodation facility" : [
            "short term crisis, emergency or transitional accommodation f"],     
          "boarding house/private hotel" : ["boarding house/private rental"],
          "none/homeless/public place" : ["none/homeless/public space"]          
        },       
    }
}

pdc = mds_aliases['fields'][M['PDC']]
mds_aliases['fields']['odc1'] = mds_aliases['fields']['odc2'] = pdc
mds_aliases['fields']['odc3'] = mds_aliases['fields']['odc4'] = pdc
mds_aliases['fields']['odc5'] = pdc

mtt = mds_aliases['fields'][M['MTT']]
mds_aliases['fields']['ott1'] = mds_aliases['fields']['ott2'] = mtt
mds_aliases['fields']['ott3'] = mds_aliases['fields']['ott4'] = mtt

mds_aliases['headers'] = {
        M['ID']      : ["pat id", "pid", "client id", "clientid"],
        M['ATSI']    : ["indig status"],
        M['CLNT_TYP']: ["client"],
        M['COMM_DATE']: ["enrolment", "commencement date", "commencement date"],
        M['COB']     : ["country"],
        M['END_DATE']: ["discharge"],
        M['DOB']    : ["date of birth"],
        M['DAI']    : ["dob accuracy", "date accuracy indicator (for dob)", "dai"],
        M['FNAME']  : ["first name", "firstname"],
        M['INJ_USE']: ["injection", "injecting drug status"],
        M['LNAME']  : ["last name", "last name"],
        M['LIVAR']  : ["living"],
        M['METHOD'] : ["use", "method of use for principal drug of concern"],
        M['MENT_HEL']: ["mental health", "mental health (diagnosed with a mental illness)"],
        M['MTT']     : ["treat", "main treatment type (mtt)"],
        M['PCODE']   : ["postcode", "postcode - australian"],
        M['PDC']     : ["drug", "pdc"],
        M['PREV_AOD']: ["previous treatment", "previous aod treatment"],
        M['PLANG']   : ["language"],
        M['REAS_CESS']: ["cessation"],
        M['SEX']     : ["sex"],
        M['SLK']     : ["slk581"],
        M['SRC_REF'] : ["source"],
        M['TDS']     : ["setting"],
        M['USACC']   : ["accom", "usual accommodation type"]
}