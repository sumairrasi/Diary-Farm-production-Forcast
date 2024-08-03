import os
from mlproject import logger
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig


import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columms =list(data.columns)
            
            all_schema = self.config.all_schema.keys()

            for col in all_columms:
                if col in all_schema:
                    if data[col].dtype == self.config.all_schema[col]:
                        validation_status = True
                    else:
                        validation_status = False
                        
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"validation status: {validation_status}")
                else:
                    
                    validation_status =False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e