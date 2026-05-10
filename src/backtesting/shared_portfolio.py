import matplotlib.pyplot as plt

from src.utils.data_loader import load_stock_data
from src.strategies.momentum_strategy import MomentumStrategy


TICKERS = ["NVDA", "AAPL", "TSLA"]
INITIAL_CASH = 10000


def run_shared_portfolio():

    strategy = MomentumStrategy()

    cash = INITIAL_CASH

    positions = {ticker: 0 for ticker in TICKERS}

    price_data = {}

    # Load all data first
    for ticker in TICKERS:
        df = load_stock_data(ticker)
        price_data[ticker] = df["Close"].astype(float).tolist()

    portfolio_curve = []

    num_days = len(price_data["NVDA"])

    for i in range(num_days):

        # Process each asset
        for ticker in TICKERS:

            prices = price_data[ticker]
            price = prices[i]

            signal = strategy.get_signal(prices, i)
            shares = positions[ticker]

            # BUY
            if signal == "BUY" and shares == 0:

                allocation = cash * strategy.get_position_size()

                if allocation > 0:
                    new_shares = allocation / price
                    positions[ticker] = new_shares
                    cash -= allocation

            # SELL
            elif signal == "SELL" and shares > 0:

                cash += shares * price
                positions[ticker] = 0

        # Portfolio valuation
        total_value = cash

        for ticker in TICKERS:
            total_value += positions[ticker] * price_data[ticker][i]

        portfolio_curve.append(total_value)

    print(f"\nFinal Portfolio Value: ${portfolio_curve[-1]:.2f}")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio_curve, label="Portfolio Value")

    plt.title("Shared Portfolio Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.legend()

    plt.show()


if __name__ == "__main__":
    run_shared_portfolio()