import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, period="1y"):
    print(f"Fetching {ticker} data...")
    data = yf.download(ticker, period=period)
    return data


def save_to_csv(data, ticker, folder="data"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, f"{ticker}.csv")

    # very important cleanup step
    data = data.reset_index()

    # make sure the structure is clean
    data.to_csv(file_path, index=False)

    print(f"Saved data to {file_path}")


if __name__ == "__main__":
    tickers = ["NVDA", "AAPL", "TSLA"]

    for ticker in tickers:
        data = fetch_stock_data(ticker)
        print(data.head())

        save_to_csv(data, ticker)