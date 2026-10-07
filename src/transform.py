import pandas as pd

def clean_data(df):

    df = df.dropna()

    df = df[df["amount"] > 0]

    df["date"] = pd.to_datetime(df["date"])

    return df