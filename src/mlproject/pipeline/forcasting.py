import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class ForcastingPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        
    def forcasting(self,start,end):
        predictions = self.model.get_prediction(start = start, end = end)
        
        return predictions
    