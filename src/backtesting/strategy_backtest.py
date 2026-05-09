from src.utils.data_loader import load_stock_data
from src.strategies.momentum_strategy import get_signal

def run_backtest(ticker, initial_cash=10000):
    df = load_stock_data(ticker)

    prices = df["Close"].tolist()

    cash = initial_cash
    shares = 0

    portfolio_values = []
    trades = 0

    peak = initial_cash
    max_drawdown = 0

    for i in range(len(prices)):
        price = float(prices[i])
        signal = get_signal(prices, i)

        # BUY
        if signal == "BUY" and cash > 0:
            shares = cash / price
            cash = 0
            trades += 1

        # SELL
        elif signal == "SELL" and shares > 0:
            cash = shares * price
            shares = 0
            trades += 1

        total_value = cash + shares * price
        portfolio_values.append(total_value)

        # Track peak for drawdown
        if total_value > peak:
            peak = total_value

        drawdown = (peak - total_value) / peak
        max_drawdown = max(max_drawdown, drawdown)

    final_value = portfolio_values[-1]
    total_return = ((final_value - initial_cash) / initial_cash) * 100

    print(f"\n--- RESULTS for {ticker} ---")
    print(f"Final Value:      ${final_value:.2f}")
    print(f"Total Return:     {total_return:.2f}%")
    print(f"Trades Executed:  {trades}")
    print(f"Max Drawdown:     {max_drawdown * 100:.2f}%")

if __name__ == "__main__":
    run_backtest("NVDA")