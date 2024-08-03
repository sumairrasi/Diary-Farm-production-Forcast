from mlproject.constants import *
from mlproject.utils.common import read_yaml, create_directories
from mlproject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataTransformationConfig,
                                            ModelTrainerConfig,
                                            ModelEvaluationConfig)




class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
         self.config = read_yaml(config_filepath)
         self.params = read_yaml(params_filepath)
         self.schema = read_yaml(schema_filepath)
         
         create_directories([self.config.artifacts_root])
    
    def data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dirs])
        
        data_ingestion_config = DataIngestionConfig(
            root_dirs = config.root_dirs,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    def data_validation_config(self) -> DataIngestionConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        
        create_directories([config.root_dirs])
        
        create_validation_config = DataValidationConfig(
            root_dirs= config.root_dirs,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )
        
        return create_validation_config
    
    def data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dirs])
        
        data_transformation_config = DataTransformationConfig(
            root_dirs=config.root_dirs,
            data_path=config.data_path
            
        )
        
        return data_transformation_config
    
    def model_trainer_config(self):
        config = self.config.model_trainer
        params = self.params.SARIMAX
        schema_target = self.schema.TARGET_COLUMN
        schema_index = self.schema.INDEX_COLUMN
        
        create_directories([config.root_dirs])
        
        model_trainer_config = ModelTrainerConfig(
            root_dirs = config.root_dirs,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            order_p= params.order_p,
            order_d = params.order_d,
            order_q = params.order_q,
            seasonal_order_p = params.seasonal_order_p,
            seasonal_order_d = params.seasonal_order_d,
            seasonal_order_q = params.seasonal_order_q,
            seasonal_order_s = params.seasonal_order_s,
            target_column = schema_target.name,
            index_column= schema_index.name
        )
        return model_trainer_config
    def model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.SARIMAX
        schema_target = self.schema.TARGET_COLUMN
        schema_index = self.schema.INDEX_COLUMN
        
        create_directories([config.root_dirs])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dirs=config.root_dirs,
            test_data_path = config.test_data_path,
            train_data_path = config.train_data_path,
            model_path= config.model_path,
            all_params = params,
            metric_file_name=config.metric_file_name,
            target_column=schema_target.name,
            index_column=schema_index.name
        )
        
        return model_evaluation_config


    
    
        
