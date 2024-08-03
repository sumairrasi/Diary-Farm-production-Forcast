import joblib
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error, mean_squared_log_error
from mlproject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from mlproject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self,actual,predictions):
        mae=mean_absolute_error(actual, predictions)
        mse=mean_squared_error(actual, predictions)
        mape = np.mean(np.abs(predictions - actual)/np.abs(actual))*100 
        return mae, mse,mape
    
    def save_results(self):
        train_data = pd.read_csv(self.config.train_data_path, parse_dates = [self.config.index_column], index_col = self.config.index_column)
        test_data = pd.read_csv(self.config.test_data_path, parse_dates = [self.config.index_column], index_col = self.config.index_column)
        model = joblib.load(self.config.model_path)
        start = len(train_data)
        end = len(train_data) + len(test_data) - 1
        predictions = model.predict(start = start, end = end, dynamic = False, typ = 'levels').rename('SARIMA Test Predictions') 
        # print(mean_absolute_error(test_data[self.config.target_column], predictions))
        mae, mse,mape = self.eval_metrics(test_data[self.config.target_column],predictions)
        print(self.eval_metrics(test_data[self.config.target_column],predictions))
        # saving metrics as local
        scores = {"MAE":mae,"MSE":mse,"MAPE":mape}
        save_json(path=Path(self.config.metric_file_name),data=scores)