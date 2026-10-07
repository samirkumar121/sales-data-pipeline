# main.py

from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_sqlite
from src.report import generate_report

df = extract_data("data/raw/sales.csv")

cleaned_df = clean_data(df)

cleaned_df.to_csv(
    "data/processed/cleaned_sales.csv",
    index=False
)

load_to_sqlite(
    cleaned_df,
    "database/sales.db"
)

generate_report(cleaned_df)