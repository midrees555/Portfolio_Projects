# Public get_data() method exposed here

import os
import pandas as pd
from dataset_manager.data_loader import DataLoader
class DataSetInterface:        
    def get_data(self, file_path):
        try:
            loader = DataLoader()
            return loader.load_data(file_path)
        except Exception as e:
            raise e     # Let test catch the real error