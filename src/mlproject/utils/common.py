import os
from box.exceptions import BoxValueError
import yaml
from mlproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content.

    Parameters:
    file_path (str): The path to the YAML file.

    Returns:
    dict: The content of the YAML file.
    """
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    
    
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def read_json_file(file_path):
    """
    Reads a JSON file and returns its content.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The content of the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except json.JSONDecodeError as exc:
        print(f"Error parsing JSON file: {exc}")
        return None
    

@ensure_annotations
def create_directories(dir_list:list, verbose=True):
    """
    Creates directories from a list of directory paths if they do not already exist.

    Parameters:
    dir_list (list): A list of directory paths to create.

    Returns:
    None
    """
    for directory in dir_list:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory '{directory}' created successfully or already exists.")
            if verbose:
                logger.info(f"Created directory at: {directory}")
        except Exception as e:
            raise e

@ensure_annotations
def save_json(path:Path, data: dict):
    
    with open(path,"w") as f:
        json.dump(data,f, indent=4)
    
    logger.info(f"json file saved at: {path}")
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations  
def load_bin(path: Path) -> Any:
    
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """
    Get the size of a file in megabytes.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    float: The size of the file in megabytes.
    """
    file_size_in_bytes = os.path.getsize(path)
    file_size_in_mb = round(file_size_in_bytes / (1024 * 1024),2)
    return f"~ {file_size_in_mb} MB"



