import pandas as pd
import os

def load_stock_data(ticker, folder="data"):
    file_path = os.path.join(folder, f"{ticker}.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No data found for {ticker}")

    df = pd.read_csv(file_path)

    if "Date" in df.columns:
        df = df[df["Date"].notna()]
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

    else:
        df = df.dropna(how="all")

    return df