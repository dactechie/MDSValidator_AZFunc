
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
from . import config, container_definition, container_options, query_options
from .SchemaProvider import SchemaProvider
import asyncio

class CosmosMongoSchemaProvider(SchemaProvider):
  def __init__(self):
      # Initialize the Cosmos client
    self.client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                        'masterKey': config['PRIMARYKEY']})
    #self.client.GetDatabaseAccount()
    db = None
    db = self.client.ReadDatabase("dbs/" + config['DATABASE'])
    # try:
    #     db = self.client.CreateDatabase({'id': config['DATABASE']})
    # except errors.HTTPFailure:
    #     db = self.client.ReadDatabase("dbs/" + config['DATABASE'])
  
    self._init_container(db)


  def _init_container(self, db):
    self.container = self.client.ReadContainer("dbs/" + db['id'] + "/colls/" + container_definition['id'])

    # Create a container
    # try:
    #   self.container = self.client.CreateContainer(db['_self'], container_definition, container_options)
    # except errors.HTTPFailure as e:
    #     if e.status_code == http_constants.StatusCodes.CONFLICT:
    #         self.container = self.client.ReadContainer("dbs/" + db['id'] + "/colls/" + container_definition['id'])
    #     else:
    #         raise e


  # def get_object_by_id(self, container_partition, id):
  #   query = {'query': f'SELECT * FROM server {container_partition} where '}

  #   result_iterable = self.client.QueryItems(self.container['_self'], query, query_options)
  #   for item in iter(result_iterable):
  #       print(item)
  async def get_schema(self):
    return await asyncio.gather(
                self.get_schema_element_by_key("main_schema"),
                self.get_schema_element_by_key("definitions")
    )

  async def build_schema(self, extras, fn_load_extras):
    # use async.io to parallelize these calls :

    schema, defs = await self.get_schema()
    for n in extras: # from local .json files
      defs["definitions"][n]  = fn_load_extras(n)
    # add country and language from local files ?
    # for n in ("countries", "drugs", "languages"): # from local .json files
    #   defs = self.load_from_file(n, defs)
    return schema, defs


  async def get_schema_element_by_key(self, data_key):
    #client.ReadItem()
    query = {'query': f'SELECT * FROM c where c.id = "{data_key}"'}
    result_iterable = self.client.QueryItems(
                      self.container['_self'], query, query_options)
    schema_obj = list(result_iterable)[0]
    return schema_obj['data']

  # def set_schema_definitions(self, validator, extra_from_files=()):
  #   defs = self.get_schema_element_by_key("definitions")
  #   # add country and language from local files ?
  #   for n in extra_from_files:
  #     defs = load_from_file(n, defs)
  #   #validator.resolver.store['/defs.json'] =  defs
