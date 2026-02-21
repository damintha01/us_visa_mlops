import yaml
import sys
from us_visa.exception import CustomException
import pickle
import numpy as np
import pandas as pd

def read_yaml(file_path: str):
    try:
        with open(file_path, "r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys)
    

def write_yaml(file_path: str, data: dict):
    try:
        with open(file_path, "w") as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
    except Exception as e:
        raise CustomException(e, sys)

def load_pickle(file_path: str):
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException(e, sys)
    

def save_numpy_array(file_path: str, array: np.ndarray):
    try:
        np.save(file_path, array)
    except Exception as e:
        raise CustomException(e, sys)


def load_numpy_array(file_path: str) -> np.ndarray:
    try:
        return np.load(file_path)
    except Exception as e:
        raise CustomException(e, sys)
    
def drop_columns(df: pd.DataFrame, cols: list):
    return df.drop(columns=cols, errors="ignore")