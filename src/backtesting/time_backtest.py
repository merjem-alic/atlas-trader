from src.utils.data_loader import load_stock_data

def run_time_backtest(ticker, initial_cash=10000):
    df = load_stock_data(ticker)

    cash = initial_cash
    shares = 0
    portfolio_values = []

    for i in range(len(df)):
        price = float(df["Close"].iloc[i])

        # buy once at start
        if i == 0:
            shares = cash / price
            cash = 0

        total_value = cash + shares * price
        portfolio_values.append(total_value)

    print(f"Final portfolio value: {portfolio_values[-1]}")

if __name__ == "__main__":
    run_time_backtest("NVDA")