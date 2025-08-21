import pandas as pd
import os
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.user = os.getenv("USERNAME","IRGC")
        self.password = os.getenv("PASSWORD","iraniraniran")
        self.db_name = os.getenv("DB_NAME","IranMalDB")
        self.col_name = os.getenv("COLLECTION_NAME","tweets")
        self.mongo_url = os.getenv("MONGO_URL","mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.col_name]

#Returning the data frame from the MongoDB collection
    def get_data_frame(self):
        data = self.collection.find()
        df = pd.DataFrame(list(data))
        return df

if __name__ == "__main__":
    conn = Connection()
    data = conn.get_data_frame()
    print(f"Found {len(data)} documents")
    print(data[:5])
