from src.strategies.base import BaseStrategy

class BuyHoldStrategy(BaseStrategy):

    def get_signal(self, prices, i):

        if i == 0:
            return "BUY"

        return "HOLD"

    def get_position_size(self):
        return 1.0