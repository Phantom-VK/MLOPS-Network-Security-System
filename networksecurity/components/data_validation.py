from networksecurity.entity.artifact_entity import DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.exception.exception import NetworkSecurityException

import sys

from networksecurity.utils.file_utils.read_yaml import read_yaml_file


class DataValidation:
    def __init__(self, data_ingestion_artifact:DataValidationArtifact, data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)