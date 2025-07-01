import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        di_config = DataIngestionConfig(training_pipeline_config)
        di = DataIngestion(di_config)
        di.initiate_data_ingestion()
    except Exception as e:
        raise NetworkSecurityException(e, sys)