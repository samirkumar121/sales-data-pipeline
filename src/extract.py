import pandas as pd
import glob

def extract_data(path):

    files = glob.glob(
        f"{path}/*.csv"
    )

    dataframes = []

    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)

    combined_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    return combined_df