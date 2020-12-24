
import copy
from ..constants import MDS, MDS_Dates, MDS_ST_FLD, MDS_END_FLD
from ...utils import v_warn_lam
'''
Input data file may not have the exact spelling/case as the official MDS fields
list_of_alias_mappings:
    [ { 'DOB' : ['Date of birth', 'DoB'] },
      { 'Principle drug of concern': ['PDC'] }
    ]
We prepare the Alias lookup table here. Result :
    {'Date of birth' : 'DOB',
        'DoB' : 'DOB',
        'PDC' : 'Principle drug of concern'
    }
'''


# reverse map header alias
#   {
#      MDS header  : aliases
#      'id' : [ "pat id", "identifier"]
#   }
#   {
# alias : MDS header
#     'pat id' : 'id',
#     'identifier': 'id'
#   }
#
#

def alias_map_lam(dict_of_alias_mappings): return {alias: official_name
                                                   for official_name, aliases in dict_of_alias_mappings.items()
                                                   for alias in aliases}


# reverse map value alias
#    MDS value :  aliases
# { "alcohol" : ["ethanol", "beer"] }
# {
#   # alias : MDS data value
#      "ethanol" : "alcohol"
#     "beer" : alcohol
# }
def alias_map_lam2(mds_dict_of_aliasedicts): return {mds_field_name: alias_map_lam(alias_dict)
                                                     for mds_field_name, alias_dict in mds_dict_of_aliasedicts.items()
                                                     }


val_translation_excluded_fields = ["enrolling provider", "eid", "age", "days enrolled", MDS["FNAME"], MDS["LNAME"],
                                   "arcadia", "treated in", MDS_ST_FLD, MDS_END_FLD, 'Odob',
                                   MDS["ID"], MDS["PCODE"], MDS["SLK"]] + [MDS[md] for md in MDS_Dates]


def translate_to_MDS_header(header, header_aliases={}):
    warnings = {}
    # [cleanse_string(h) for h in header]
    converted_header = copy.deepcopy(header)
    headers_map = alias_map_lam(header_aliases)
    for i, h in enumerate(header):
        hlow = h  # .lower()
        # {alias1 : official_k1}, {alias2 : official_k1}, ...
        if hlow in headers_map:
            # save the official MDS value in the new header
            converted_header[i] = headers_map[hlow]
            warnings[h] = headers_map[hlow]
            #warnings[f"Header uses key:{h} instead of {headers_map[hlow]}"] = 1

    return converted_header, warnings


# without the deep copy
def translate_to_MDS_values(data, fields_aliases={}):
    warnings = []
    fields_to_check = [k for k in data[0]
                       if k not in val_translation_excluded_fields]
    fields_map = alias_map_lam2(fields_aliases)

    falias = {key: alias_dict for key,
              alias_dict in fields_map.items() if key in fields_to_check}

    # each row                          [ {row1}, {row2}  {ID: 2}]
    for i, ddict in enumerate(data):
        # for data_key, v in ddict.items(): # each field within a row     row1->  { k1:v1 , k2:v2}
        for data_key in fields_to_check:
            v = ddict[data_key]
            conv_data_val = v.strip()
            if data_key in falias and conv_data_val in falias[data_key]:
                conv_data_val = falias[data_key][conv_data_val]
                warnings.append(
                    v_warn_lam(i, ddict[MDS['ID']], conv_data_val, v)
                )
            data[i][data_key] = conv_data_val

    return warnings
