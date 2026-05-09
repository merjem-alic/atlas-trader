from src.utils.data_loader import load_stock_data

tickers = ["NVDA", "AAPL", "TSLA"]

for ticker in tickers:
    print(f"\nLoading {ticker}...")

    data = load_stock_data(ticker)

    print(data.head())