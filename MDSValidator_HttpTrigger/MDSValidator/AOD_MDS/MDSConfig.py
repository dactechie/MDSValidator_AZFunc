import json

from .constants import MDS as M
from ...CommonUtils import constants as DBConstants
from ...logger import logger

def process_loaded_config(config):
    mds_data_value_aliases, mds_header_aliases = map_to_mds_values(
        config[DBConstants.DB_KEY_ALIASES])
    # we don't store duplicates for similar fields, it is done on the fly
    create_copy_aliases(mds_data_value_aliases)
    config[DBConstants.DB_KEY_ALIASES] = {

        "fields": mds_data_value_aliases,
        "headers": mds_header_aliases
    }
    return config

def map_to_mds_values(config_dict):
    return [
        {M[k]: alias_dict for k, alias_dict in config_dict['fields'].items()},
        {M[k]: alias_list for k, alias_list in config_dict['headers'].items()}
    ]

def create_copy_aliases(mds_aliases):

    pdc_aliases = mds_aliases[M['PDC']]
    mds_aliases['odc1'] = mds_aliases['odc2'] = pdc_aliases
    mds_aliases['odc3'] = mds_aliases['odc4'] = pdc_aliases
    mds_aliases['odc5'] = pdc_aliases

    mtt_aliases = mds_aliases[M['MTT']]
    mds_aliases['ott1'] = mds_aliases['ott2'] = mtt_aliases
    mds_aliases['ott3'] = mds_aliases['ott4'] = mtt_aliases


class MDSLocalConfigurationLoader:

    def __init__(self, config_loading_client):
        if not config_loading_client:
            raise ValueError("Config loading client was not defined")

        self.config_client = config_loading_client
        self.config = {}

    ##
    #
    # Aliases
    # MethodOfUseMatrix
    #

    def load_config(self, schema_domain):
        # https://github.com/rgl/azure-content/blob/master/articles/storage/storage-python-how-to-use-table-storage.md
        # https://pypi.org/project/azure-data-tables/#description
        # parameters = {"pk1": schema_domain}
        # filterValue = "(PartitionKey eq @pk1) and IsActive"
        # result = self.config_client.query_entities(filter=filterValue, parameters=parameters)
        
        logger.debug (f'Going to load Alias config from URL '\
                      f'{self.config_client.url} and '\
                      f'Table {self.config_client.table_name}')

        filter_str = f"PartitionKey eq '{schema_domain}' or PartitionKey eq 'Common' and IsActive"
        logger.debug(filter_str)
        result = self.config_client.query_entities(filter=filter_str)
                
        rlist = list(result)
        # logger.debug(f"result list {rlist}")
        for r in rlist:
            self.config[r.get("RowKey")] = json.loads(r.get("Value"))

    def get_config(self, schema_domain):
        if(self.config):
            return self.config
        else:
            self.load_config(schema_domain)
            self.config = process_loaded_config(self.config)
            logger.debug(f"Loaded remote config. MethodOfUseMatrix:"\
                                     f"{self.config['MethodOfUseMatrix']}")
            logger.debug(f"Loaded remote config. Headers: "\
                                    f"{self.config['Aliases']['headers']}")
            return self.config
