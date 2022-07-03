from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from settings.config import CONFIG


client = MongoClient(CONFIG.database.get_connection_url())
db = client[CONFIG.database.database]


def check_connection():
    try:
        client.server_info()
    except ConnectionFailure:
        return False

    return True
