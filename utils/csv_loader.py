import pandas as pd

def load_csv_as_df(csv_path):
    df = pd.read_csv(csv_path)
    # Optional: Drop unused or label columns if unsupervised
    df = df.dropna()
    df = df.select_dtypes(include=["number"])
    return df
