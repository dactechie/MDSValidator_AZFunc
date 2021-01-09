
import pytest
#from AOD_MDS.helpers import  translate_to_MDS_header, translate_to_MDS_values
from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.constants import MDS as M
from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.helpers.translators import (
            translate_to_MDS_header, translate_to_MDS_values)
from MDSValidator_HttpTrigger.MDSValidator.logger import logger
from MDSValidator_HttpTrigger.MDSValidator.AOD_MDS.MDSConfig import map_to_mds_values


ACTMDSAliases = {
        "fields":{"ATSI":{"neither aboriginal nor torres strait islander origin":["neither aboriginal nor tsi","not indigenous"],"aboriginal but not torres strait islander origin":["aboriginal but not tsi","aboriginal"],"torres strait islander but not aboriginal origin":["tsi but not aboriginal"],"both aboriginal and torres strait islander origin":["both aboriginal and tsi"]},"COB":{"vietnam":["viet nam"],"serbia":["serbia and montenegro"],"arabic":["arabic (including lebanese)"],"british antarctic territory":["british antarctic"],"myanmar":["burma (myanmar)","burma (republic of the union of myanmar)"],"england":["united kingdom"]},
      "CLNT_TYP":{"own alcohol or other drug use":["own drug use","own alcohol or other drug  use"],"other's alcohol or other drug use":["other's drug use","other's alcohol/other drug use"]},
      "DAI":{"aaa - day, month and year are accurate":["aaa"],"eee - day, month and year are estimated":["eee"],"uue - day and month are unknown, year is estimated":["uue"],"uuu - day, month and year are unknown":["uuu"],"eea - day and month are estimated, year is accurate":["eea"]},
      "INJ_USE":{"not stated/inadequately described":["not stated / inadequately described"],"last injected more than twelve months ago":["injecting drug use more than 12 months ago","injecting drug use more than twelve months ago (and not in last twelve months)"],"last injected three months ago or less":["current injecting drug use (last injectected prev 3 months)","current injecting drug use (last injected within the previous three months)"],"last injected more than three months ago but less than or equal to twelve months ago":["injecting drug use between 3 to 12 months ago","injecting drug use more than three months ago but less than twelve months ago"]},      
      "LIVAR":{"friend(s)/parent(s)/relative(s) and child(ren)":["friend(s)/parent(s)/relative(s) and chil(ren)"],
      "spouse/partner and child(ren)":["spouse/partner and child(ren)"],"alone":["alone"],"other relative(s)":["other relative(s)"],
      "not known/inadequately described":["not stated / inadequately described"]},
      "MENT_HEL":{"not stated/inadequately described":["not stated / inadequately described"],"diagnosed more than twelve months ago":["diagnosed more than 12 months ago"],"diagnosed three months ago or less":["diagnosed 3 months ago or less"],"never been diagnosed":["not diagnosed, displaying possible symptoms"],"diagnosed more than three months ago but less than or equal to twelve months ago":["diagnosed between 3 months and 12 months ago","diagnosed more than three months ago or less than or equal to twelve month ago"]},"METHOD":{"not stated/inadequately described":["not stated"],"ingests":["ingest"],"smokes":["smoke"],"injects":["inject"],"sniffs (powder)":["sniff (powder)"],"inhales (vapour)":["inhale (vapour)"]},"MTT":{"counselling":["dats counselling"],"support and case management":["support & case management only"]},"PDC":{"not stated/inadequately described":["not stated / inadequately described"],"heroin":["heroin"],"opioid antagonists, n.e.c.":["opioid antagonists, nec","opioid antagonists nfd"],"methamphetamine":["crystal(meth) / ice / methamphetamine /speed","ice"],"lysergic acid diethylamide":["lsd","lyserfic acid diethylamide"],"alcohol":["alcohol","ethanol","alcohol /ethanol"],"mdma":["ecstasy (mdma)"],"cannabinoids":["cannabis","cannabinoids and related drugs nfd","cannabinoids (cannabis)"],"nicotine":["nicotine/tobacco"],"amphetamines nfd":["amphetamines","amphetamines, nfd"],"benzodiazepines nfd":["benzodiazepines","benzodiazepines, nfd"],"analgesics nfd":["other analgesics"],"other stimulants and hallucinogens, n.e.c.":["other stimulants/hallucinogens"],"other sedatives and hypnotics, n.e.c.":["sedatives and hypnotics nfd","other sedatives/hypnotics"],"ghb type drugs and analogues, n.e.c.":["ghb type drugs and analogues nfd","ghb type drugs and analogues, nec"],"synthetic opioid analgesics, n.e.c.":["synthetic opioid analgesics nfd"],"opioid analgesics nfd":["opoid analgesics nfd"],"anabolic androgenic steroids, n.e.c.":["anabolic androgenic steroids nfd"],"psychostimulants":["psychostimulants nfd"],"other antidepressants and antipsychotics, n.e.c.":["antidepressants and antipsychotics nfd"]},"REAS_CESS":{"treatment completed":["treatment completed","episode resolved"],"ceased to participate at expiation":["ceased at expiation"],"ceased to participate against advice":["ceased against advice"],"ceased to participate without notice":["ceased without notice"],"ceased to participate by mutual agreement":["ceased by mutual agreement"],"ceased to participate involuntary (non-compliance)":["ceased involuntary"],"change in main treatment type":["change in the main treatment type"],"change in principal drug of concern":["change in the principal drug of concern"],"change in delivery setting":["change in the delivery setting"],"transferred to another service provider":["transferred to other provider"],"imprisoned, other than drug court sanctioned":["imprisoned (not drug court)"],"other":["other reason for cessation"]},"PREV_AOD":{"withdrawal management (detoxification)":["withdrawal management (detoxification)","withdrawl management (detoxification)"],"residential treatment facility":["residential treatment facility"],"no previous treatment received":["no treatment"]},"SRC_REF":{"medical practitioner":["medical practitioner"],"correctional service":["correctional service"],"family member/friend":["family member/friend"],"alcohol and other drug treatment service":["alcohol & other drug treatment"],"other community/health care service":["other community/health service"]},"TDS":{"outreach setting":["outreach setting"],"private residence":["private residence","rented private house or flat","rented public house or flat"],"non-residential treatment facility":["non-residential facility"]},"USACC":{"private residence":["rented public house or flat","rented private house or flat"],"alcohol and other drugs":["alcohol/other drug treatment residence"],"short term crisis, emergency or transitional accommodation facility":["short term crisis, emergency or transitional accommodation f"],"boarding house/private hotel":["boarding house/private rental"],"none/homeless/public place":["none/homeless/public space"]}},
     
      "headers":{"ID":["pat id","pid","client id","clientid"],"ATSI":["indig status"],
      "CLNT_TYP":["client"],"COMM_DATE":["enrolment","commencement date","commencement date"],
      "COB":["country"],"END_DATE":["discharge"],"DOB":["date of birth"],"DAI":["dob accuracy","date accuracy indicator (for dob)","dai"],"FNAME":["first name","firstname"],"INJ_USE":["injection","injecting drug status"],"LNAME":["last name","last name"],"LIVAR":["living"],"METHOD":["use","method of use for principal drug of concern"],"MENT_HEL":["mental health","mental health (diagnosed with a mental illness)"],"MTT":["treat","main treatment type (mtt)"],"PCODE":["postcode","postcode - australian"],"PDC":["drug","pdc"],"PREV_AOD":["previous treatment","previous aod treatment"],"PLANG":["language"],"REAS_CESS":["cessation"],"SEX":["sex"],"SLK":["slk581"],"SRC_REF":["source"],"TDS":["setting"],"USACC":["accom","usual accommodation type"]
      }
  }
    

mds_data_value_aliases, mds_header_aliases = map_to_mds_values(ACTMDSAliases)

# pytest  tests/test_helpers.py::test_translate_to_MDS_header -vv
@pytest.mark.parametrize("header, expected", 
                          [( # ["pid", "method of use for principal drug of concern" ],["id", "method of use for pdc"],
                            [ # NSW MDS spreadsheet headers
                              "pid",	"last name",	"first name",	"slk 581",	"sex",	"date of birth",	"date accuracy indicator (for dob)",	"country of birth",	"indigenous status",
                              "preferred language",	"postcode - australian",	"usual accommodation",	"client type",	"source of referral",	"principal source of income",	"commencement date",
                              "end date",	"reason for cessation",	"referral to another service",	"treatment delivery setting",	"method of use for principal drug of concern",	"injecting drug status",
                              "pdc",	"main treatment type (mtt)",	"living arrangements",	"previous aod treatment",	
                              "mental health (diagnosed with a mental illness)"],

                              #  Expected : from constants:
                              ["id", "surname", "first name", "slk 581", "sex",	'dob', "date accuracy indicator", "country of birth", "indigenous status",
                              "preferred language", "postcode (australian)",
                              "usual accommodation",	"client type", "source of referral", "principal source of income","commencement date",
                              "end date",	"reason for cessation", "referral to another service" , "treatment delivery setting", "method of use for pdc",
                              "injecting drug use status", "principle drug of concern",	"main treatment type",	"living arrangements",	
                              "previous alcohol and other drug treatment received", "mental health"]                                	                            
                          )]
                        )
def test_translate_to_MDS_header(header, expected):    
    converted_header, warnings = translate_to_MDS_header(header, mds_header_aliases)
    logger.info(warnings)
    assert converted_header == expected


@pytest.mark.parametrize("data, expected, expected_warnings", 
                          [( # testing the field_values map as well..
                            [{ 'id': '101010',  'client type': "own drug use" }], 
                            {'client type':"own alcohol or other drug use", 'id': '101010'}, 
                            { "index": 0, "cid": '101010', "required": "own alcohol or other drug use", "got": "own drug use"}
                          ),
                          ( [{ 'id': '12354',  'client type': "other's drug use" }], 
                            {'client type':"other's alcohol or other drug use", 'id': '12354'}, 
                            { "index": 0, "cid": '12354', "required": "other's alcohol or other drug use",
                              "got": "other's drug use"}
                          )
                        ])
def test_translate_to_MDS_values(data, expected, expected_warnings):
    warnings = translate_to_MDS_values(data, mds_data_value_aliases)
    logger.info(warnings)

    assert data[0] == expected
    
    assert warnings[0] == expected_warnings
