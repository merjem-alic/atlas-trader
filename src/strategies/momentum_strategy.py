from src.strategies.base import BaseStrategy

class MomentumStrategy(BaseStrategy):

    def get_signal(self, prices, i):
        if i < 2:
            return "HOLD"

        today = prices[i]
        yesterday = prices[i - 1]
        day_before = prices[i - 2]

        if today > yesterday > day_before:
            return "BUY"

        if today < yesterday < day_before:
            return "SELL"

        return "HOLD"