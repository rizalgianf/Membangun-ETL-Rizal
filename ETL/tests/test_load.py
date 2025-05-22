import pytest
import pandas as pd
import os
from utils.load import load_to_database, load_to_csv

def test_load_to_database():
    # Assuming we have a mock database and data to test
    mock_data = {'id': 1, 'name': 'Test'}
    result = load_to_database(mock_data)
    assert result is True  # Adjust based on actual function return value

def test_load_to_csv(tmp_path):
    df = pd.DataFrame({'id': [1], 'name': ['Test']})
    file_path = tmp_path / "output.csv"
    load_to_csv(df, file_path)
    assert os.path.exists(file_path)
    # Optional: cek isi file jika perlu