import sys

import numpy as np
import pandas as pd

from networksecurity.entity.artifact_entity import DataIngestionArtifact
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

## Configuration of the data ingestion config

from networksecurity.entity.config_entity import DataIngestionConfig
import os
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.mongo_client = None
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_df(self):
        """
        Read dataframe from mongodb
        :return:
        Database data as a pandas dataframe
        """
        try:
            logging.info("Exporting Data from Mongodb")
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df = df.drop(columns="_id", axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            logging.info("Exporting Data to feature store")
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test_spllit(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split on data")
            train_dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            test_dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(train_dir_path, exist_ok=True)
            os.makedirs(test_dir_path, exist_ok=True)
            logging.info("Created test and training dirs")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False,
                header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False,
                header=True
            )
            logging.info("Exported training and test set")

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_df() # Get data frommongodb
            logging.info("Exported Data from Mongodb")
            dataframe = self.export_data_into_feature_store(dataframe) # Store it locally as csv
            logging.info("Exported Data to feature store")
            self.split_data_as_train_test_spllit(dataframe)
            di_artifact = DataIngestionArtifact(training_file_path=self.data_ingestion_config.training_file_path,
                                                test_file_path=self.data_ingestion_config.training_file_path)
            logging.info("Created data ingestion artifact")
            return di_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)