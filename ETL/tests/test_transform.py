import pandas as pd
import pytest
from utils.transform import transform_function_1, transform_function_2, transform_products  # Replace with actual function names

def test_transform_function_1():
    input_data = [...]  # Replace with test input data
    expected_output = [...]  # Replace with expected output
    assert transform_function_1(input_data) == expected_output

def test_transform_function_2():
    input_data = [...]  # Replace with test input data
    expected_output = [...]  # Replace with expected output
    assert transform_function_2(input_data) == expected_output

def test_transform_products():
    data = {
        "Title": ["T-shirt", "Unknown Product"],
        "Price": ["$10", "$0"],
        "Rating": ["4.5 / 5", "Invalid Rating"],
        "Colors": ["3 Colors", "0 Colors"],
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

# Add more tests as needed for other transformation functions