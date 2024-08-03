import os
from mlproject import logger
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config
        
        
    def train_test_split(self):
        df = pd.read_csv(self.config.data_path, parse_dates = ['Date'], index_col = 'Date')
        train = df[:int(0.85*(len(df)))]
        test = df[int(0.85*(len(df))):]
        
        train.to_csv(os.path.join(self.config.root_dirs,"train.csv"))
        test.to_csv(os.path.join(self.config.root_dirs,"test.csv"))
        
        logger.info("Splitted data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)