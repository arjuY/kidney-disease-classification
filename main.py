from disease_classifier import logger
from disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"======= stage {STAGE_NAME} started =======")
    ingestion = DataIngestionTrainingPipeline()
    ingestion.main()
    logger.info(f"======= stage {STAGE_NAME} completed =======")
except Exception as e:
    logger.exception(e)
    raise e