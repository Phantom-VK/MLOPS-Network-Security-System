import logging
import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, \
    DataTransformationConfig, ModelTrainerConfig

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

        dt_config = DataTransformationConfig(training_pipeline_config)
        dt = DataTransformation(data_transformation_config=dt_config, data_validation_artifact=dv_artifact)
        logging.info("Initiated data transformation")
        dt_artifact = dt.initiate_data_transformation()
        print(dt_artifact)

        mt_config = ModelTrainerConfig(training_pipeline_config)
        mt = ModelTrainer(model_trainer_config=mt_config, data_transformation_artifact=dt_artifact)
        logging.info("Initiated model training")
        mt_artifact = mt.initiate_model_trainer()
        print(mt_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)




