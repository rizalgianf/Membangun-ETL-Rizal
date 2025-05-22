def load_to_database(data, connection_string):
    import pandas as pd
    from sqlalchemy import create_engine

    # Create a database engine
    engine = create_engine(connection_string)

    # Load data into the database
    data.to_sql('table_name', con=engine, if_exists='replace', index=False)

def load_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")