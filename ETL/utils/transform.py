import pandas as pd

def clean_price(price_str):
    # Contoh: "$25" -> 400000
    try:
        price = float(price_str.replace("$", "").replace(",", "").strip())
        return int(price * 16000)
    except:
        return None

def clean_rating(rating_str):
    # Contoh: "⭐ 3.9 / 5" -> 3.9
    try:
        if "⭐" in rating_str:
            rating_str = rating_str.replace("⭐", "").strip()
        return float(rating_str.split("/")[0].strip())
    except:
        return None

def clean_colors(colors_str):
    # Contoh: "3 Colors" -> 3
    try:
        return int(colors_str)
    except:
        return None

def clean_size(size_str):
    # Contoh: "Size: M" -> "M"
    return size_str.replace("Size:", "").strip()

def clean_gender(gender_str):
    # Contoh: "Gender: Unisex" -> "Unisex"
    return gender_str.replace("Gender:", "").strip()

def transform_products(df):
    df = df.copy()
    df["Price"] = df["Price"].apply(clean_price)
    df["Rating"] = df["Rating"].apply(clean_rating)
    df["Colors"] = df["Colors"].apply(clean_colors)
    df["Size"] = df["Size"].apply(clean_size)
    df["Gender"] = df["Gender"].apply(clean_gender)

    # Hapus data invalid
    df = df.dropna()
    df = df[df["Title"].str.lower() != "unknown product"]
    df = df[df["Rating"] > 0]
    df = df[df["Price"] > 0]
    df = df[df["Colors"] > 0]
    df = df[df["Size"] != ""]
    df = df[df["Gender"] != ""]

    # Hapus duplikat
    df = df.drop_duplicates()

    # Pastikan tipe data
    df = df.astype({
        "Title": str,
        "Price": int,
        "Rating": float,
        "Colors": int,
        "Size": str,
        "Gender": str,
        "Timestamp": str
    })

    return df

def transform_data(data):
    # Example transformation: Clean and filter the data
    cleaned_data = [item for item in data if item is not None and item != '']
    return cleaned_data

def aggregate_data(data):
    # Example aggregation: Sum numerical values
    return sum(data)

def filter_data(data, condition):
    # Example filtering: Return items that meet a certain condition
    return [item for item in data if condition(item)]