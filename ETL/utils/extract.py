import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_products(pages=50):
    base_url = "https://fashion-studio.dicoding.dev"
    products = []

    for page in range(1, pages + 1):
        url = base_url if page == 1 else f"{base_url}/page{page}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")
        except Exception as e:
            print(f"[ERROR] Gagal mengambil halaman {url}: {e}")
            continue

        for card in soup.select("div.product-details"):
            try:
                title_tag = card.select_one("h3.product-title")
                price_tag = card.select_one("span.price")
                p_tags = card.find_all("p")

                title = title_tag.get_text(strip=True) if title_tag else ""
                price = price_tag.get_text(strip=True) if price_tag else ""
                rating, colors, size, gender = "", "", "", ""
                for p in p_tags:
                    text = p.get_text(strip=True)
                    if "Rating:" in text:
                        rating = text.replace("Rating:", "").strip()
                    elif "Colors" in text:
                        colors = text.replace("Colors", "").strip()
                    elif "Size:" in text:
                        size = text.replace("Size:", "").strip()
                    elif "Gender:" in text:
                        gender = text.replace("Gender:", "").strip()
                timestamp = datetime.utcnow().isoformat()
                products.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "Timestamp": timestamp
                })
            except Exception as e:
                print(f"[ERROR] Gagal memproses produk pada halaman {page}: {e}")
                continue
    return pd.DataFrame(products)

def extract_from_csv(file_path):
    return pd.read_csv(file_path)

def extract_from_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def extract_from_database(connection_string, query):
    from sqlalchemy import create_engine

    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)