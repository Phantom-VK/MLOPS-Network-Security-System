import os
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