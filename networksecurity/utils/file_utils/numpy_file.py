import os
import pickle
import sys

import numpy as np

from networksecurity.exception.exception import NetworkSecurityException


def save_numpy_array_data(file_path:str, array:np.array):
    """
    Save numpy array data to file
    :param file_path: str location of the file to save
    :param array: np.array data to save
    :return:
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            np.save(file_path, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


def load_numpy_array_data(file_path:str) -> object:
    """
    load numpy array data from file
    :param file_path: str location of file to load
    :return: np.array data loaded
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file {file_path} does not exists")
        with open(file_path, 'rb') as file_obj:
            print(file_obj)
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)