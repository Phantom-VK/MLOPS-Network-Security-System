# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

#
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
#
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


class NetworkDataExtract:
    def __init__(self):
        self.collection = None
        self.database = None
        self.records = None
        self.mongo_client = None
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongo(self, records, database, collection):
        try:
            self.database = database
            self.collection  = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "temp_network_data/phisingData.csv"
    Database = "NetworkSecurityProject"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(FILE_PATH)

    no_of_records = networkobj.insert_data_to_mongo(records, Database, Collection)
    print(no_of_records)

