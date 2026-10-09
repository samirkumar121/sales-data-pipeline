# main.py

from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_sqlite
from src.report import generate_report
from src.logger import logger
from src.data_quality import validate_data

logger.info("Pipeline Started")

df = extract_data(
    "data/raw"
)
print(df)
validate_data(df)
logger.info(f"Extracted {len(df)} rows")
logger.info(f"Extracted {len(df)} rows")
cleaned_df = clean_data(df)
logger.info(f"Cleaned {len(cleaned_df)} rows")
cleaned_df.to_csv(
    "data/processed/cleaned_sales.csv",
    index=False
)

load_to_sqlite(
    cleaned_df,
    "database/sales.db"
)
logger.info("Data loaded to SQLite")
generate_report(cleaned_df)
logger.info("Pipeline Completed")