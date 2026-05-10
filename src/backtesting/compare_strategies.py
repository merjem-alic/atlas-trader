import matplotlib.pyplot as plt

from src.utils.data_loader import load_stock_data
from src.strategies.momentum_strategy import MomentumStrategy
from src.strategies.buy_hold import BuyHoldStrategy

FEE_RATE = 0.001
SLIPPAGE = 0.0005


def run_backtest(strategy, prices, initial_cash=10000):
    cash = initial_cash
    shares = 0

    peak = initial_cash
    max_drawdown = 0
    trades = 0

    equity_curve = []

    for i in range(len(prices)):
        price = float(prices[i])
        signal = strategy.get_signal(prices, i)

        if signal == "BUY" and shares == 0:
            allocation = cash * strategy.get_position_size()
            execution_price = price * (1 + SLIPPAGE)

            shares = allocation / execution_price
            cash -= allocation

            trades += 1

        elif signal == "SELL" and shares > 0:
            execution_price = price * (1 - SLIPPAGE)

            cash += shares * execution_price
            cash -= cash * FEE_RATE

            shares = 0

            trades += 1

        total = cash + shares * price
        equity_curve.append(total)

        if total > peak:
            peak = total

        drawdown = (peak - total) / peak
        max_drawdown = max(max_drawdown, drawdown)

    final_value = cash + shares * float(prices[-1])

    return {
        "final_value": final_value,
        "return_pct": (final_value - initial_cash) / initial_cash * 100,
        "trades": trades,
        "max_drawdown": max_drawdown * 100,
        "equity_curve": equity_curve
    }


def compare():
    df = load_stock_data("NVDA")
    prices = df["Close"].astype(float).tolist()

    strategies = {
        "Momentum": MomentumStrategy(),
        "BuyHold": BuyHoldStrategy()
    }

    results = {}

    for name, strat in strategies.items():
        print(f"\nRunning {name}...")
        results[name] = run_backtest(strat, prices)

    print("\n--- COMPARISON ---")
    for name, r in results.items():
        print(f"\n{name}")
        print(f"Return: {r['return_pct']:.2f}%")
        print(f"Trades: {r['trades']}")
        print(f"Drawdown: {r['max_drawdown']:.2f}%")

    plot_results(results)


def plot_results(results):
    plt.figure(figsize=(12, 6))

    for name, data in results.items():
        plt.plot(data["equity_curve"], label=name)

    plt.title("Strategy Comparison - Equity Curves")
    plt.xlabel("Time (Days)")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    compare()