import pandas as pd
import os
from mlproject import logger
from statsmodels.tsa.statespace.sarimax import SARIMAX
from mlproject.entity.config_entity import ModelTrainerConfig
import joblib

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
        
    def train(self):
        print("index column :",self.config.index_column)
        print("target column :",self.config.target_column)
        train_data = pd.read_csv(self.config.train_data_path, parse_dates = [self.config.index_column], index_col = self.config.index_column)
        test_data = pd.read_csv(self.config.test_data_path, parse_dates = [self.config.index_column], index_col = self.config.index_column)
        model = SARIMAX(train_data[self.config.target_column],
                order = (self.config.order_p,
                         self.config.order_d,
                         self.config.order_q),
                seasonal_order = (self.config.seasonal_order_p,
                                  self.config.seasonal_order_d,
                                  self.config.seasonal_order_q,
                                  self.config.seasonal_order_s))
        results = model.fit(disp = False)
        joblib.dump(results, os.path.join(self.config.root_dirs,self.config.model_name))