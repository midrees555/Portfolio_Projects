# |========== Importing essential libraries ==========|

import os
import pytest
import pandas as pd
from dataset_manager.data_loader import DataLoader
from dataset_manager.dataset_interface import DataSetInterface

# Paths to test files (Make sure these exist in /tests or /sample_data)
VALID_CSV = "tests/sample_data/sample.csv"
VALID_XLSX = "tests/sample_data/sample.xlsx"
INVALID_FILE = "tests/sample_data/unsupported.txt"
MISSING_FILE = "tests/sample_data/not_found.csv"

def test_load_valid_csv():
    loader = DataLoader()
    df = loader.load_data(VALID_CSV)
    
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    
def test_get_data_missing_file():
    interface = DataSetInterface()
    
    with pytest.raises(Exception):
        interface.get_data(MISSING_FILE)