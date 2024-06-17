from src.cnnClassifier.logger import logging
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logging.info(f">>> Stage:  {STAGE_NAME} started <<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>> Stage: {STAGE_NAME} completed <<<")

except Exception as e:
    raise e