import os
from pymongo import MongoClient


class MongoFetcher:
    def __init__(self):
        # Load environment variables for MongoDB connection
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        dbname = os.getenv("MONGO_DBNAME")
        host = os.getenv("MONGO_HOST")

        uri = f"mongodb+srv://{user}:{password}@{host}/{dbname}?retryWrites=true&w=majority"
        self.client = MongoClient(uri)
        self.db = self.client[dbname]
        self.collection = self.db["tweets"]  # שם הקולקשן שלך, תעדכן אם שונה

    def fetch_all(self):
        return list(self.collection.find())
