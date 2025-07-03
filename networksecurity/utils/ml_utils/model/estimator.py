import os
import sys

from networksecurity.constant.training_pipeline import SAVED_MODE_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self, preprocesor, model):
        try:
            self.preprocesor = preprocesor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def predict(self, x):
        try:
            x_transformed = self.preprocesor.transform(x)
            y_hat = self.model.predict(x_transformed)

            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys)



