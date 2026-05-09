from src.utils.data_loader import load_stock_data

def run_simple_backtest(ticker, initial_cash=10000):
    print(f"\nRunning simple backtest for {ticker}...")

    # Load cleaned data
    df = load_stock_data(ticker)

    # Get first and last price
    first_price = float(df["Close"].iloc[0])
    last_price = float(df["Close"].iloc[-1])

    print(f"Buy price: {first_price}")
    print(f"Sell price: {last_price}")

    # How many shares we can buy
    shares = initial_cash / first_price

    final_value = shares * last_price

    profit = final_value - initial_cash
    return_pct = (profit / initial_cash) * 100

    print("\n--- RESULT ---")
    print(f"Initial cash: ${initial_cash:.2f}")
    print(f"Final value:  ${final_value:.2f}")
    print(f"Profit:       ${profit:.2f}")
    print(f"Return:       {return_pct:.2f}%")

if __name__ == "__main__":
    run_simple_backtest("NVDA")