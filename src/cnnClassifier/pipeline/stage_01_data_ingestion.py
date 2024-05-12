from cnnClassifier.config.configuration import configurationManager
from cnnClassifier.components.data_ingestion import DataIngetion
from cnnClassifier.logger import logging

STAGE_NAME= "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
       
        config=configurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingetion=DataIngetion(config=data_ingestion_config)
        data_ingetion.extract_zipfile()

if __name__=='__main__':
    try:
        logging.info(f">>> Stage:  {STAGE_NAME} started <<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>> Stage: {STAGE_NAME} completed <<<")

    except Exception as e:
        raise e