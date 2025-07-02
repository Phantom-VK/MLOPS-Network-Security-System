import logging
import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        di_config = DataIngestionConfig(training_pipeline_config)
        di = DataIngestion(di_config)
        logging.info("Initiating the data ingestion")
        di_artifact = di.initiate_data_ingestion()

        dv_config = DataValidationConfig(training_pipeline_config)
        dv = DataValidation(data_ingestion_artifact=di_artifact, data_validation_config=dv_config)
        logging.info("Initiating the data validation")
        dv_artifact = dv.initiate_data_validation()
        print(dv_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)




