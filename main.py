from disease_classifier import logger
from disease_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from disease_classifier.pipeline.stage_02_base_model import BaseModelTrainingPipeline
from disease_classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"======= stage {STAGE_NAME} started =======")
    ingestion = DataIngestionTrainingPipeline()
    ingestion.main()
    logger.info(f"======= stage {STAGE_NAME} completed =======")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Preparing base model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = BaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e