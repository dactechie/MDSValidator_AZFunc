from .constants import MDS as M

mds_aliases = {
    # k (official name) : v [] -> array of aliases or accepted values

    "fields":{
        M['ATSI']: {        
          "Neither Aboriginal nor Torres Strait Islander origin": ["Neither Aboriginal nor TSI"],
          "Aboriginal but not Torres Strait Islander origin": ["Aboriginal but not TSI"],
          "Torres Strait Islander but not Aboriginal origin": ["TSI but not Aboriginal"],
          "Both Aboriginal and Torres Strait Islander origin": ["Both Aboriginal and TSI"],
        },
        M['COB']: {
          "Vietnam" : ["Viet Nam"],
          "Serbia" : ["Serbia and Montenegro"],
          "Arabic" : ["Arabic (Including Lebanese)"],
          "British Antarctic Territory" : ["British Antarctic"],
          "Myanmar" : ["Burma (Myanmar)", "Burma (Republic of the Union of Myanmar)"],        
        },        
        M['CLNT_TYP']:{
          "Own alcohol or other drug use": ["Own drug use" ],
          "Other's alcohol or other drug use": ["Other's drug use", "Other's alcohol/other drug use"],        
        },
        M['DAI']: {
          "AAA - Day, month and year are accurate":[ "AAA" ],
          "EEE - Day, month and year are estimated":[ "EEE" ],
          "UUE - Day and month are unknown, year is estimated": ["UUE"],
          "UUU - Day, month and year are unknown":      ["UUU"],        
          "EEA - Day and month are estimated, year is accurate" : ["EEA"],
        },
        M['INJ_USE'] : {
          "Not stated/inadequately described" : ["Not stated / inadequately described"],
          "Last injected more than twelve months ago":[
              "Injecting drug use more than 12 months ago",
              "Injecting drug use more than twelve months ago (and not in last twelve months)"],
          "Last injected three months ago or less": [
              "Current injecting drug use (last injectected prev 3 months)",
              "Current injecting drug use (last injected within the previous three months)"],
          "Last injected more than three months ago but less than or equal to twelve months ago": [ 
              "Injecting drug use between 3 to 12 months ago",
              "Injecting drug use more than three months ago but less than twelve months ago"]
        },
        M['LIVAR']: {          
          "Friend(s)/parent(s)/relative(s) and child(ren)" : ["Friend(s)/parent(s)/relative(s) and chil(ren)"],
          "Spouse/partner and child(ren)" : ["Spouse/partner and Child(ren)"], 
          "Alone" : ["alone"],
          "Other relative(s)" : ["Other Relative(s)"], # TODO check me Family memner/friend eqiuivalemtr
          "Not known/inadequately described": ["Not Stated / Inadequately Described"]
        },        
        M['MENT_HEL']: {
          "Not stated/inadequately described" : ["Not Stated / Inadequately Described" ],
          "Diagnosed more than twelve months ago": ["Diagnosed more than 12 months ago"],        
          "Diagnosed three months ago or less" : ["Diagnosed 3 months ago or less"],        
          "Never been diagnosed": [ "Not Diagnosed, displaying possible symptoms"],
          "Diagnosed more than three months ago but less than or equal to twelve months ago": [
            "Diagnosed between 3 months and 12 months ago",
            "Diagnosed more than three months ago or less than or equal to twelve month ago"
          ],
        },
        M['METHOD'] :{
          "Not stated/inadequately described" : ["Not Stated"]
        },        
        M['MTT'] : {
          "Counselling" : [ "DATS Counselling" ],
          "Support and case management": ["Support & case management only"],
        #  "Support and case management": ["Support and case management only", "Support & case management only"],
        #  "Information and education" : [ "Information and education only"],
         # "Assessment": ["Assessment only"]
        },
        M["PDC"]: {
              "Not stated/inadequately described" :["Not Stated / Inadequately Described"],
              "Heroin": ["heroin"],
              "Opioid Antagonists, n.e.c." : ["Opoid Analgesics nfd","Opioid Analgesics nfd"],
              "Methamphetamine" : ["Crystal(meth) / Ice / Methamphetamine /Speed"],   # Coordinare Sep 2019 ; MJ's common Drugs translation
              "Lysergic acid diethylamide": ["LSD"],
              "Alcohol": ["alcohol", "Ethanol"  , "Alcohol /Ethanol" ],
              "MDMA": ["Ecstasy (MDMA)"],
              "Cannabinoids" : ["cannabinoids", "Cannabis", "Cannabinoids and Related Drugs nfd"],
              "Diazepam": ["diazepam"],
              "Nicotine" : ["nicotine", "Nicotine/tobacco"],
              "Codeine": ["codeine"],
              "Amphetamines nfd" : [ "Amphetamines", "Amphetamines, nfd" ],
              "Benzodiazepines nfd" : ["Benzodiazepines"],
              "Analgesics nfd" : ["Other analgesics"],
              "Stimulants and Hallucinogens nfd" : [ "Other stimulants/hallucinogens"],
              "Sedatives and Hypnotics nfd": ["Other sedatives/hypnotics"],
              "GHB type Drugs and Analogues, n.e.c." :["GHB type Drugs and Analogues nfd"],
        },
        M['REAS_CESS']: {
          "Ceased to participate against advice": ["Ceased against advice"],
          "Ceased to participate without notice" : ["Ceased without notice"],
          "Ceased to participate by mutual agreement": ["Ceased by mutual agreement"],
          "Ceased to participate involuntary (non-compliance)": ["Ceased involuntary"],
          "Change in main treatment type" : ["Change in the main treatment type"],          
          "Change in delivery setting" : ["Change in the delivery setting"],
          "Transferred to another service provider" : ["Transferred to other provider"],
          "Imprisoned, other than drug court sanctioned":["Imprisoned (not drug court)" ],
          "Other" : ["Other reason for cessation"]
        },
        M['PREV_AOD']:{          
          "Withdrawal management (detoxification)" : ["Withdrawal Management (detoxification)", "Withdrawl management (detoxification)"],     
          "Residential treatment facility" : ["Residential Treatment Facility"],
          "No previous treatment received" : ["No treatment"],                
        },
        M['SRC_REF']:{
          "Medical Practitioner": ["Medical practitioner"],
          "Correctional service" : ["Correctional Service"],
          "Family member/friend" : ["Family member/Friend"],
          "Alcohol and other drug treatment service": ["Alcohol & other drug treatment"],
          "Other Community/health care service" : ["Other community/health service"]
        },
        M['TDS']:{
          "Outreach setting" : ["Outreach Setting"],
          "Private residence" : ["Private Residence", "Rented private house or flat",
                                 "Privately owned house or flat", "Rented public house or flat"],
          "Non-residential treatment facility" :["Non-residential Facility"]
        },
        M['USACC']:{
          "Private residence": ["Rented public house or flat"],
          "Short term crisis, emergency or transitional accommodation facility" : [
            "Short term crisis, emergency or transitional accommodation f"],
          "Other specialised community residential": ["Other specialised community residential"],        
          "Boarding house/private hotel" : ["Boarding house/private rental"],
          "None/homeless/public place" : ["None/homeless/public space"],
          
        },       
    }
}

pdc = mds_aliases['fields'][M['PDC']]
mds_aliases['fields']['ODC1'] = mds_aliases['fields']['ODC2'] = pdc
mds_aliases['fields']['ODC3'] = mds_aliases['fields']['ODC4'] = pdc
mds_aliases['fields']['ODC5'] = pdc

mtt = mds_aliases['fields'][M['MTT']]
mds_aliases['fields']['OTT1'] = mds_aliases['fields']['OTT2'] = mtt
mds_aliases['fields']['OTT3'] = mds_aliases['fields']['OTT4'] = mtt

mds_aliases['headers'] = {
        M['ID']      : ["PAT ID", "PID", "Client ID", "ClientID"],
        M['ATSI']    : ["INDIG STATUS"],
        M['CLNT_TYP']: ["CLIENT"],
        M['COMM_DATE']: ["ENROLMENT", "Commencement Date", "Commencement date"],
        M['COB']     : ["COUNTRY"],
        M['END_DATE']: ["DISCHARGE"],
        M['DOB']    : ["Date of birth"],
        M['DAI']    : ["DOB ACCURACY", "Date accuracy indicator (for DoB)", "DAI"],
        M['FNAME']  : ["First Name", "Firstname"],
        M['INJ_USE']: ["INJECTION", "Injecting drug status"],
        M['LNAME']  : ["Last Name", "Last name"],
        M['LIVAR']  : ["LIVING"],
        M['METHOD'] : ["USE", "Method of use for principal drug of concern"],
        M['MENT_HEL']: ["MENTAL HEALTH", "Mental health (Diagnosed with a mental illness)"],
        M['MTT']     : ["TREAT", "Main treatment type (MTT)"],
        M['PCODE']   : ["POSTCODE", "Postcode - Australian"],
        M['PDC']     : ["DRUG", "PDC"],
        M['PREV_AOD']: ["PREVIOUS TREATMENT", "Previous AOD treatment"],
        M['PLANG']   : ["LANGUAGE"],
        M['REAS_CESS']: ["CESSATION"],
        M['SEX']     : ["SEX"],
        M['SLK']     : ["SLK581"],
        M['SRC_REF'] : ["SOURCE"],
        M['TDS']     : ["SETTING"],
        M['USACC']   : ["ACCOM", "Usual accommodation type"]
}