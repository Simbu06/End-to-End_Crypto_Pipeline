import requests
import time
from pymongo import MongoClient, UpdateOne
from datetime import datetime

client = MongoClient('mongodb+srv://silambarsan:simbu007@cluster0.4auu8z9.mongodb.net/?appName=Cluster0')
db = client['crypto_data']
collection = db['Data']

def fetch_crypto_data():

    url = "https://api.coingecko.com/api/v3/coins/markets"
    pages = 10

    for page in range(1, pages + 1):

        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'precision': 2,
            'per_page': 50,
            'page': page,
        }

        max_retries = 5
        backoff = 5

        for attempt in range(max_retries):

            response = requests.get(url, params=params)

            if response.status_code == 200:
                print(f"Page {page} → 200 OK")

                data = response.json()
                op = []   

                for coin in data:
                    coin["last_updated"] = datetime.now()
                    coin["currency"] = "USD"

                    op.append(
                        UpdateOne(
                            {"id": coin["id"]},
                            {"$set": coin},
                            upsert=True
                        )
                    )

                if op:
                    collection.bulk_write(op)

                break  

            elif response.status_code == 429:
                print(f"Rate limited. Waiting {backoff}s (attempt {attempt+1})")
                time.sleep(backoff)
                backoff *= 2  

            else:
                print(f"Error {response.status_code}")
                break

        time.sleep(3) 


if __name__ == "__main__":
    fetch_crypto_data()
