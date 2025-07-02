import logging
import os.path

import pandas as pd
from scipy.stats import ks_2samp

from networksecurity.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.exception.exception import NetworkSecurityException

import sys

from networksecurity.utils.file_utils.yaml import read_yaml_file, write_yaml_file


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return  pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_number_of_columns(self, dataframe:pd.DataFrame) -> bool:
        try:
            number_of_columns = len(self._schema_config.get("columns"))
            df_columns = len(dataframe.columns)
            logging.info(f"Required Columns: {number_of_columns}   Dataframe columns: {df_columns}")

            return df_columns == number_of_columns

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def is_numerical_column_exist(self, dataframe:pd.DataFrame) -> bool:
        try:
            number_of_numerical_columns =  len(self._schema_config.get("numerical_columns"))
            df_numerical_columns = sum([1 for col in dataframe.columns if dataframe[col].dtype == int])

            logging.info(f"Required numerical columns: {number_of_numerical_columns}  Dataframe numerical columns: {df_numerical_columns}")

            return number_of_numerical_columns == df_numerical_columns
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataframe_drift(self, base_df:pd.DataFrame, current_df:pd.DataFrame, threshold = 0.05) -> bool:
        try:
            status = True
            report = {}

            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_sample_dist = ks_2samp(d1, d2)
                if threshold <= is_sample_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({
                    column:{
                        "p_value":float(is_sample_dist.pvalue),
                        "drift_status":is_found
                    }
                })
                drift_report_file_path = self.data_validation_config.drift_report_file_path
                dir_path = os.path.dirname(drift_report_file_path)
                os.makedirs(dir_path, exist_ok=True)

                write_yaml_file(drift_report_file_path, report)
            return status

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.training_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            ## Read data from train and test data path
            train_dataframe = self.read_data(train_file_path)
            test_dataframe = self.read_data(test_file_path)

            ## Validate columns
            logging.info("Validating total columns")
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                train_error_message = f"Train dataframe does not contains all columns!"
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                test_error_message = f"Test dataframe does not contains all columns!"

            logging.info("Validating numerical columns")
            status = self.is_numerical_column_exist(dataframe=train_dataframe)
            if not status:
                train_error_message = f"Train dataframe does not contains all numerical columns!"
            status = self.is_numerical_column_exist(dataframe=test_dataframe)
            if not status:
                test_error_message = f"Test dataframe does not contains all numerical columns!"

            logging.info("Detecting Drift Status")
            status = self.detect_dataframe_drift(base_df=train_dataframe, current_df=test_dataframe)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Drift status: {status}")

            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path, index=False, header=True
            )
            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path, index=False, header=True
            )
            logging.info("Exported test and train dataframes to valid file paths")
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_test_file_path= "",
                invalid_train_file_path= "",
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )
            logging.info("Data validation completed")
            return data_validation_artifact


        except Exception as e:
            raise NetworkSecurityException(e, sys)