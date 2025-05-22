import pandas as pd
from utils.extract import extract_products
from utils.transform import transform_products
from utils.load import load_to_csv

def main():
    print("Extracting data...")
    df = extract_products()
    print(f"Extracted {len(df)} rows.")
    if df.empty:
        print("No data extracted. Please check your extract function and website structure.")
        return
    print("Transforming data...")
    df_clean = transform_products(df)
    print(f"Cleaned data: {len(df_clean)} rows.")
    print("Saving to CSV...")
    load_to_csv(df_clean)
    print("ETL process completed.")

df = extract_products()
print(df.head(10))
print(df.dtypes)

if __name__ == "__main__":
    main()