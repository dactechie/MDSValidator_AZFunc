import os
import logging

from azure.data.tables import TableServiceClient


class AZTableService:

    def __init__(self, table_name="MDSValidatorMappings"):
        account_uri = os.environ['MDSValidatorMappingStorage_URI']
        sas_token = os.environ['MDSValidatorMappingStorage_SAS']

        table_service_client = TableServiceClient(
            account_url=account_uri, credential=sas_token)
        self.table_client = table_service_client.get_table_client(table_name)
        if self.table_client:
            logging.debug("loaded table client")
        else:
            logging.error(" couldnt load table client for remote config")

    def get(self):
        return self.table_client
