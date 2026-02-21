import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL_KEY = "MONGODB_URL"
DATABASE_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

PIPELINE_NAME: str = "us_visa"
ARTIFACTS_DIR: str = "artifacts"
FILE_NAME: str = "EasyVisa.csv"
MODEL_FILE_NAME = "model.pkl"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

DATA_INGESTION_COLLECTION_NAME: str ="visa_data"
DATA_INGESTION_DIR_NAME:str ="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


