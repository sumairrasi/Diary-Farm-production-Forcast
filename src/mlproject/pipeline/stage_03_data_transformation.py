from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1].strip()
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation = config.data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation)
                    data_transformation.train_test_split()
                else:
                    raise Exception("Your data schema is not valid")
        except Exception as e:
            raise e