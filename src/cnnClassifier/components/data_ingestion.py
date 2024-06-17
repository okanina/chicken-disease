import os
import zipfile
from pathlib import Path
import urllib.request as request
from cnnClassifier.logger import logging
from cnnClassifier.entity.config_entity import DataIngestionConfig
# from cnnClassifier.constants import *
from cnnClassifier.utils.common import *

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)

            logging.info(f"{filename} downloaded! with following info \n{headers}")
        else:
            logging.info(f"file already exist of size {get_size(Path(self.config.local_data_file))}")


    def extract_zipfile(self):

        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)