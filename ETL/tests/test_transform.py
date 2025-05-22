import pandas as pd
from utils.transform import transform_products

def test_transform_products():
    data = {
        "Title": ["T-shirt", "Unknown Product"],
        "Price": ["$10", "$0"],
        "Rating": ["4.5 / 5", "Invalid Rating"],
        "Colors": ["3", "0"],
        "Size": ["Size: M", "Size: "],
        "Gender": ["Gender: Unisex", "Gender: "],
        "Timestamp": ["2024-01-01T00:00:00", "2024-01-01T00:00:00"]
    }
    df = pd.DataFrame(data)
    df_clean = transform_products(df)
    assert len(df_clean) == 1
    assert df_clean.iloc[0]["Title"] == "T-shirt"
    assert df_clean.iloc[0]["Price"] == 160000
    assert df_clean.iloc[0]["Rating"] == 4.5
    assert df_clean.iloc[0]["Colors"] == 3
    assert df_clean.iloc[0]["Size"] == "M"
    assert df_clean.iloc[0]["Gender"] == "Unisex"