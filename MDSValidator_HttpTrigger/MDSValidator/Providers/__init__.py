
import urllib3
urllib3.disable_warnings()

config = {
    'ENDPOINT': 'https://localhost:8081',
    'PRIMARYKEY': 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==',
    'DATABASE': 'CosmosDatabase',
    #'CONTAINER': 'CosmosContainer'
    'CONTAINER' : 'ANSAResponses'
}

# # Create container options
container_options = {
    'offerThroughput': 400
}

container_definition = {
    'id': config['CONTAINER']
}

query = {'query': 'SELECT * FROM server c'}

query_options = {}
query_options['enableCrossPartitionQuery'] = True
query_options['maxItemCount'] = 2
