import pandas as pd
import os
from utils.load import load_to_csv

def test_load_to_csv(tmp_path):
    df = pd.DataFrame({'id': [1], 'name': ['Test']})
    file_path = tmp_path / "output.csv"
    load_to_csv(df, file_path)
    assert os.path.exists(file_path)
    # Cek isi file
    loaded = pd.read_csv(file_path)
    assert loaded.iloc[0]['id'] == 1
    assert loaded.iloc[0]['name'] == 'Test'