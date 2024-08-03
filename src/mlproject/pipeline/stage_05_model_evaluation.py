from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger


STAGE_NAME = "Model Evaluation  Stage"

class   ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        mode_evalution_config = config.model_evaluation_config()
        mode_evalution_config = ModelEvaluation(config=mode_evalution_config)
        mode_evalution_config.save_results()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========================================x")
    except Exception as e:
        logger.exception(e)
        raise e