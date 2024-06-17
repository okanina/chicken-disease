import yaml
import os
from ensure import ensure_annotations
import base64
import joblib
from typing import Any
import json
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from src.cnnClassifier.logger import logging

@ensure_annotations
def read_yaml(path_to_yaml: Path):
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            return ConfigBox(content)        
    # except BoxValueError:
    #     raise  ValueError("no data.")
    except Exception as e:
        raise e
    
@ensure_annotations   
def create_directories(path_to_directories:list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logging.info(f"Created directory at {path}")
@ensure_annotations
def save_json(path:Path, data:dict):

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Json file saved at path:{path}")

@ensure_annotations
def load_json(path: Path):

    with open(path) as f:
        content=json.load(f)

    logging.info(f"Successfully loaded json file from {path}")
    return ConfigBox[content]

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logging.info(f"Binary file saved as {path}")

@ensure_annotations
def load_bin(path: Path):

    data=joblib.load(path)
    logging.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path:Path):

    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring, filename):
    imgdata=base64.b64encode(imgstring)
    with open(filename, "wb") as f:
        f.read(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())



