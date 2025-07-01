import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd


TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
NETWORK_DATA_FILE: str ="temp_network_data/phisingData.csv"

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkSecurityProject"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingestion"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2