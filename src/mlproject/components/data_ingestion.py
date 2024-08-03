import os
import requests
import zipfile
from mlproject import logger
from mlproject.utils.common import get_size
from mlproject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        """Download the file from source_url if it does not exist locally."""
        if not os.path.exists(self.config.local_data_file):
            print(self.config.local_data_file)
            print(self.config.source_url)
            response = requests.get(self.config.source_url, stream=True)
            if response.status_code == 200:
                with open(self.config.local_data_file, 'wb') as f:
                    f.write(response.content)
                print(f"{self.config.local_data_file} downloaded!")
            else:
                print(f"Failed to download file, status code: {response.status_code}")
        else:
            print(f"File already exists of size: {get_size(self.config.local_data_file)}")
    
    
    def extract_zip_file(self):
        """
        Extracts a ZIP file to the specified directory.

        Parameters:
        zip_file_path (str): The path to the ZIP file.
        extract_to_dir (str): The directory to extract the files to.

        Returns:
        None
        """
        zip_file_path = self.config.local_data_file
        extract_to_dir = self.config.unzip_dir
        # Check if the ZIP file exists
        print("zip file path:",zip_file_path)
        if not os.path.isfile(zip_file_path):
            raise FileNotFoundError(f"The file {zip_file_path} does not exist.")
        
        # Check if the extraction directory exists, if not, create it
        if not os.path.exists(extract_to_dir):
            os.makedirs(extract_to_dir)
        
        # Extract the ZIP file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)

        print(f"Files extracted to {extract_to_dir}")