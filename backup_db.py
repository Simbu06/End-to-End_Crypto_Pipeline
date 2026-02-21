import pandas as pd
from pymongo import MongoClient, UpdateOne
from sqlalchemy import create_engine, text
import time


# Mongo
MONGO_ATLAS_URI = "mongodb+srv://silambarsan:simbu007@cluster0.4auu8z9.mongodb.net/?appName=Cluster0"
LOCAL_MONGO_URI = "mongodb://simbu:simbu007@localhost:27017/"

MONGO_DB = "crypto_data"
MONGO_COLLECTION = "Data"
UNIQUE_FIELD = "id"

# PostgreSQL
NEON_URI = "postgresql://neondb_owner:npg_50sJkdwHtPRU@ep-hidden-frost-a72vc2id-pooler.ap-southeast-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
LOCAL_PG_URI = "postgresql://simbu:simbu007@localhost:5432/mydb"

PG_TABLE = "crypto_data"



def backup():
    print("🔄 Backing up MongoDB...")

    cloud_client = MongoClient(MONGO_ATLAS_URI)
    local_client = MongoClient(LOCAL_MONGO_URI)

    cloud_col = cloud_client[MONGO_DB][MONGO_COLLECTION]
    local_col = local_client[MONGO_DB][MONGO_COLLECTION]

    data = list(cloud_col.find())

    operations = []

    for doc in data:
        doc.pop("_id", None)
        operations.append(
            UpdateOne(
                {UNIQUE_FIELD: doc[UNIQUE_FIELD]},
                {"$set": doc},
                upsert=True
            )
        )

    if operations:
        local_col.bulk_write(operations)

    print(f"✅ Mongo backup completed ({len(data)} records synced)")
    
    time.sleep(3)
    
    print("🔄 Backing up PostgreSQL...")

    cloud_engine = create_engine(NEON_URI)
    local_engine = create_engine(LOCAL_PG_URI)

    df = pd.read_sql(f"SELECT * FROM {PG_TABLE}", cloud_engine)

    print(f"Cloud rows fetched: {len(df)}")

    with local_engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {PG_TABLE} RESTART IDENTITY"))

    df.to_sql(
        PG_TABLE,
        local_engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print("✅ PostgreSQL backup completed")


def main():
    print("🚀 Backup started...")
    backup()
    print("🎯 Backup finished successfully.")


if __name__ == "__main__":
    main()