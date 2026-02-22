
from extract import fetch_crypto_data
from transform import transform_crypto_data
from load import load_data_to_db
from test import test
from backup_db import backup
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "logs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(OUTPUT_DIR / "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        logging.info("Pipeline started")

        backup()
        logging.info("Backup completed")

        fetch_crypto_data()
        logging.info("Extract completed")

        transform_crypto_data()
        logging.info("Transform completed")

        test()
        logging.info("Test completed")

        load_data_to_db()
        logging.info("Load completed")

        logging.info("Pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
