# |========== Importig essential libraries ==========|
import pandas as pd
import os

class DataLoader:
    def __init__(self):
        pass
    
    def load_data(self, file_path):
        """
        Loada a dataset from a CSV or Excel file and returns a Dataframe.
        Raises appropriate errors for unsupported formats or failed reads.
        """
        
        try:
            if not os.path.exists(file_path):
                raise FileExistsError(f"❌ File not found: '{file_path}'")
            
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
            else:
                raise ValueError("❌ Unsupported file format!")
            
            if df.empty:
                raise ValueError("Dataset is empty!")
            
            return df
        except Exception as e:
            raise e     # Let the caller handle/log it