# Handles CSV/Excel loading using abstraction

import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def load_data(self):
        try:
            if self.file_path.endswith('.csv'):
                df = pd.read_csv(self.file_path)
                
            elif self.file_path.endswith('.xlsx'):
                df = pd.read_excel(self.file_path)
                
            else:
                raise ValueError("Unsupported file format!")
            
            if df.empty:
                raise ValueError("The dataset is empty")
            
            print("\n📄 Data Preview: (First 5 Rows):")
            print(df.head())
            
            return df
        
        except FileNotFoundError:
            print(f"❌ File not found: {self.file_path}")
            
        except ValueError as ve:
            print(f"❌ Value Error: {ve}")
            
        except Exception as e:
            print(f"❌ An unexpected error occured: {e}")