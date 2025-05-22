import pandas as pd
import pytest
from utils.extract import extract_from_csv, extract_from_api, extract_products

def test_extract_from_csv():
    # Assuming the function returns a DataFrame
    data = extract_from_csv('path/to/test.csv')
    assert data is not None
    assert len(data) > 0  # Check that data is not empty

def test_extract_from_api():
    # Assuming the function returns a dictionary
    data = extract_from_api('https://api.example.com/data')
    assert data is not None
    assert 'key' in data  # Check that the expected key is in the response

def test_extract_products(monkeypatch):
    # Mock requests.get agar tidak benar-benar melakukan HTTP request
    class MockResponse:
        @staticmethod
        def raise_for_status():
            pass
        text = '''
        <div class="card-product">
            <h2 class="card-title">T-shirt</h2>
            <span class="card-price">$10</span>
            <span class="card-rating">4.5 / 5</span>
            <span class="card-colors">3 Colors</span>
            <span class="card-size">Size: M</span>
            <span class="card-gender">Gender: Unisex</span>
        </div>
        '''
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    df = extract_products()
    assert isinstance(df, pd.DataFrame)
    assert "Title" in df.columns
    assert "Price" in df.columns
    assert len(df) > 0