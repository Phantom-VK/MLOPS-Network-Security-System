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


def load_object(file_path:str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file {file_path} does not exists")
        with open(file_path, 'rb') as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
