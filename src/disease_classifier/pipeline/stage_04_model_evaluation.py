import os
from disease_classifier import logger
from disease_classifier.components.model_evaluation import Evaluation
from disease_classifier.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()