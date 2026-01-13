import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
from pathlib import Path

class KaggleLoader():
    """
    A class to load CSV datasets from Kaggle
    """
    def __init__(self, dataset_url: str):
        self.dataset_url = dataset_url

    def load_csv(self, file: str):
        """
        Load CSV from Kaggle dataset (UTF-8 only)
        
        :param file: CSV file name inside the Kaggle dataset
        :type file: str
        """
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            self.dataset_url,
            file
        )
        return df
    
    def load_csv_with_encoding(self, file: str, encoding: str) -> pd.DataFrame:
        """
        Load CSV with custom encoding by downloading the dataset locally
        """
        dataset_path = Path(
            kagglehub.dataset_download(self.dataset_url)
        )

        file_path = dataset_path / file
        return pd.read_csv(file_path, encoding = encoding)