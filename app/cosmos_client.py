import uuid
from azure.cosmos import CosmosClient, PartitionKey, ConsistencyLevel
from datetime import datetime

class CosmosDBClient:
    def __init__(self):
        self.endpoint = os.getenv('COSMOS_ENDPOINT')
        self.key = os.getenv('COSMOS_KEY')
        self.database_name = os.getenv('COSMOS_DB')
        self.container_name = os.getenv('COSMOS_CONTAINER')

        self.client = CosmosClient(self.endpoint, credential=self.key)
        self.database = self.client.get_database_client(self.database_name)
        self.container = self.database.get_container_client(self.container_name)

    def write_item(self, value):
        item = {
            'id': str(uuid.uuid4()),
            'value': value,
            'timestamp': datetime.utcnow().isoformat()
        }
        self.container.create_item(item)

    def read_latest_item(self, consistency_level):
        client = CosmosClient(
            self.endpoint,
            credential=self.key,
            consistency_level=getattr(ConsistencyLevel, consistency_level)
        )
        container = client.get_database_client(self.database_name).get_container_client(self.container_name)
        items = list(container.query_items(
            query="SELECT * FROM c ORDER BY c._ts DESC",
            enable_cross_partition_query=True
        ))
        return items[0] if items else None
