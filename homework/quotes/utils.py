import configparser
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('../config.ini')

USER = config.get('DB', 'USER')
PASS = config.get('DB', 'PASS')
DB_NAME = config.get('DB', 'DB_NAME')
DOMAIN = config.get('DB', 'DOMAIN')


def get_mongodb():
    # client = MongoClient("mongodb+srv://nik160186:<password>@mymongo.x4hv9eh.mongodb.net/?retryWrites=true&w=majority")
    client = MongoClient(f"mongodb+srv://{USER}:{PASS}@{DOMAIN}.x4hv9eh.mongodb.net/?retryWrites=true&w=majority")
    db = client.book
    return db



