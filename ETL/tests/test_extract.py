import pandas as pd
import pytest
from utils.extract import extract_products

def test_extract_products(monkeypatch):
    # Mock requests.get agar tidak benar-benar melakukan HTTP request
    class MockResponse:
        @staticmethod
        def raise_for_status():
            pass
        text = '''
        <div class="product-details">
            <h3 class="product-title">T-shirt</h3>
            <span class="price">$10</span>
            <p>Rating: 4.5 / 5</p>
            <p>3</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
        '''
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    df = extract_products(pages=1)
    assert isinstance(df, pd.DataFrame)
    assert "Title" in df.columns
    assert "Price" in df.columns
    assert "Rating" in df.columns
    assert "Colors" in df.columns
    assert "Size" in df.columns
    assert "Gender" in df.columns
    assert len(df) > 0
    assert df.iloc[0]["Title"] == "T-shirt"
    assert df.iloc[0]["Price"] == "$10"
    assert df.iloc[0]["Rating"] == "4.5 / 5"
    assert df.iloc[0]["Colors"] == "3"
    assert df.iloc[0]["Size"] == "M"
    assert df.iloc[0]["Gender"] == "Unisex"