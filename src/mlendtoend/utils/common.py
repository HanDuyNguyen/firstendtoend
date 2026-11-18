import json
import os
from pathlib import Path
from typing import Any, List

import joblib
import yaml
from box import ConfigBox

from src.mlendtoend import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and return

    Args:
        path_to_yaml (str): path to the yaml file

    Returns:
        ConfigBox: Parsed content of the yaml file, allowing dot-notation access
    
    Raises:
        Exception: if any error occurs while reading or parsing the file
    """
    try:
        with open(path_to_yaml, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"Load yaml file from {path_to_yaml} succesfully")
            return ConfigBox(content)
    except Exception as e:
        raise e

def create_directories(path_to_directories: List[str]):
    """Create directories from a list

    Args:
        path_to_directories: list of directories to be created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Create a directory at {path}")


def save_json(path: Path, data: dict):
    """Save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json 
    """

    with open(path, 'w') as f:
        json.dump(data, f)

    logger.info(f"json file is saved at {path}")


def load_json(path: Path) -> ConfigBox:
    """Load json file

    Args: 
        path (Path): path to json file

    Returns:
        ConfigBox: parsed content of json     
    """

    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"Successfully load json file at {path}")

    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    """Save binary file

    Args:
        data (Any): data to be saved
        path (Path): path to binary file 
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at {path}")


def load_bin(path: Path) -> Any:
    """Load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in file
    """

    data = joblib.load(path)
    logger.info(f"Successfully load binary file at {path}")
    return data


if __name__=="__main__":
    params = read_yaml(Path("params.yaml"))
    print(params)
    create_directories(['xxxx'])
    params = load_json("test.json")
    print(params)
