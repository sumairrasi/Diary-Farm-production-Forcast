from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dirs: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dirs: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dirs: Path
    data_path: Path
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dirs: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    order_p: int
    order_d: int
    order_q: int
    seasonal_order_p: int
    seasonal_order_d: int
    seasonal_order_q: int
    seasonal_order_s: int
    target_column: str
    index_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dirs: Path
    train_data_path: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    index_column: str
    