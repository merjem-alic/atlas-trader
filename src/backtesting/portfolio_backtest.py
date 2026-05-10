import matplotlib.pyplot as plt

from src.utils.data_loader import load_stock_data
from src.strategies.momentum_strategy import MomentumStrategy

TICKERS = ["NVDA", "AAPL", "TSLA"]

def run_portfolio_backtest():

    strategy = MomentumStrategy()

    portfolio_results = {}
    total_equity = None

    for ticker in TICKERS:

        print(f"\nRunning backtest for {ticker}...")

        df = load_stock_data(ticker)
        prices = df["Close"].astype(float).tolist()

        cash = 10000
        shares = 0

        equity_curve = []

        for i in range(len(prices)):

            price = prices[i]
            signal = strategy.get_signal(prices, i)

            if signal == "BUY" and shares == 0:

                allocation = cash * strategy.get_position_size()

                shares = allocation / price
                cash -= allocation

            elif signal == "SELL" and shares > 0:

                cash += shares * price
                shares = 0

            total = cash + shares * price
            equity_curve.append(total)

        final_value = cash + shares * prices[-1]

        portfolio_results[ticker] = {
            "equity_curve": equity_curve,
            "final_value": final_value
        }

        print(f"{ticker} Final Value: ${final_value:.2f}")

    return portfolio_results


def plot_portfolio(results):

    plt.figure(figsize=(12, 6))

    for ticker, data in results.items():

        plt.plot(data["equity_curve"], label=ticker)

    plt.title("Multi-Asset Portfolio Backtest")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)

    plt.show()


if __name__ == "__main__":

    results = run_portfolio_backtest()

    plot_portfolio(results)