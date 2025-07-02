import pickle
import sys
import os
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

def save_object(file_path:str, obj:object) -> None:
    try:
        logging.info("Entered Save Object method of generic utils")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
        logging.info("Exited Save Object method of generic utils")
    except Exception as e:
        raise NetworkSecurityException(e, sys)