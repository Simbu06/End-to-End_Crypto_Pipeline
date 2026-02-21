import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db():

    try:
        engine = create_engine('postgresql://neondb_owner:npg_50sJkdwHtPRU@ep-hidden-frost-a72vc2id-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require')
        df = pd.read_csv("transformed_crypto_data.csv")

        df.to_sql('crypto_data', engine, if_exists='replace', index=False)

        print('Data inserted successfully into the database.')
        
    except Exception as e:
        print(f'Error inserting data into the database: {e}')

if __name__ == "__main__":
    load_data_to_db()