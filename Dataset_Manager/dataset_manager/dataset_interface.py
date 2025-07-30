# Public get_data() method exposed here

import os
import pandas as pd

class DataSetInterface:        
    def get_data(self, file_path):
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
                return data
            elif file_path.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(file_path)
                return data
            else:
                raise ValueError("Unsupported file format!")
            
        except Exception as e:
            print(f"❌ Failed to load file: {e}")
            return None