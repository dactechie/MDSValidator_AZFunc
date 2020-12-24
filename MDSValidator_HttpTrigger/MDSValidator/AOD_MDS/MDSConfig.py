import json

from .constants import MDS as M
from ...CommonUtils import constants as DBConstants


class MDSLocalConfigurationLoader:

    def __init__(self, config_loading_client):
        if not config_loading_client:
            raise ValueError("Config loading client was not defined")

        self.config_client = config_loading_client
        self.config = {}

    def load_config(self, schema_domain):
        # https://github.com/rgl/azure-content/blob/master/articles/storage/storage-python-how-to-use-table-storage.md
        # https://pypi.org/project/azure-data-tables/#description
        # parameters = {
        #    "pk": 'Local' #schema_domain           
        # }
        # filterValue = "PartitionKey eq @pk and IsActive"
        # result = self.config_client.query_entities(filter=filterValue, parameters=parameters)

        result = self.config_client.query_entities(filter="IsActive")
        # parameters = {
        #     "active": true
        # }
        # filterValue = "IsActive eq @active"
        # result = self.config_client.query_entities(
        #     filter=filterValue, parameters=parameters)

        # filterValue = ""  # PartitionKey eq 'Local' and RowKey eq 'MethodOfUseMatrix'"
        # #batch  = table_client.create_batch() #result = table_client.query_entities(filter="PartitionKey eq 'Local'")
        # result = self.config_client.query_entities(filter=filterValue)

        rlist = list(result)
        for r in rlist:
            self.config[r.get("RowKey")] = json.loads(r.get("Value"))

        mds_data_value_aliases, mds_header_aliases = self.map_to_mds_values()
        # we don't store duplicates for similar fields, it is done on the fly
        self.create_copy_aliases(mds_data_value_aliases)
        self.config[DBConstants.DB_KEY_ALIASES] = {

            "fields": mds_data_value_aliases,
            "headers": mds_header_aliases

        }
        return self.config

    def map_to_mds_values(self):
        data_value_aliases = self.config[DBConstants.DB_KEY_ALIASES]['fields']
        header_aliases = self.config[DBConstants.DB_KEY_ALIASES]['headers']

        return [
            {M[k]: alias_dict for k, alias_dict in data_value_aliases.items()},
            {M[k]: alias_list for k, alias_list in header_aliases.items()}
        ]

    def create_copy_aliases(self, mds_aliases):

        pdc_aliases = mds_aliases[M['PDC']]
        mds_aliases['odc1'] = mds_aliases['odc2'] = pdc_aliases
        mds_aliases['odc3'] = mds_aliases['odc4'] = pdc_aliases
        mds_aliases['odc5'] = pdc_aliases

        mtt_aliases = mds_aliases[M['MTT']]
        mds_aliases['ott1'] = mds_aliases['ott2'] = mtt_aliases
        mds_aliases['ott3'] = mds_aliases['ott4'] = mtt_aliases

    def get_config(self, schema_domain):
        if(self.config):
            return self.config
        else:
            return self.load_config(schema_domain)
