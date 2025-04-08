from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["threats"]

def store_if_new(item):
    if not collection.find_one({"title": item["title"]}):
        collection.insert_one(item)
        return True
    return False
