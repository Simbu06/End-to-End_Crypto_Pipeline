import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://simbu:simbu007@localhost:27017/')
db = client['crypto_data']
collection = db['Data']

def transform_crypto_data():
    data = list(collection.find({}, {'_id': 0}))
    df = pd.DataFrame(data)

    df = df[
        [
            'id',
            'symbol',
            'name',
            'current_price',
            'market_cap',
            'total_volume',
            'high_24h',
            'low_24h',
            'price_change_percentage_24h',
            'last_updated'
        ]
    ]
    
    

    df = df.rename(columns={
        "price_change_percentage_24h": "pct_change_24h"
    })

    df['pct_change_24h'] = df['pct_change_24h'].round(2)

    df['total_volume'] = df['total_volume'].fillna(0)
    
    df['high_24h'] = df['high_24h'].fillna(0)
    
    df['low_24h'] = df['low_24h'].fillna(0)
    
    df['pct_change_24h'] = df['pct_change_24h'].fillna(0)   


    col_change = [
        'current_price',
        'market_cap',
        'total_volume',
        'high_24h',
        'low_24h',
        'pct_change_24h'
    ]

    for col in col_change:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.drop_duplicates(subset=['id'], keep='first')
    df = df.sort_values(by='market_cap', ascending=False)
    df = df.reset_index(drop=True)

    df = df[
        (df['current_price'] > 0) &
        (df['market_cap'] >= 0) &
        (df['total_volume'] >= 0)
    ]

    df.to_csv('transformed_crypto_data.csv', index=False)
    
    print('Data transformation completed successfully.')
    
if __name__ == "__main__":
    transform_crypto_data()