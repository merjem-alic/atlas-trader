class BaseStrategy:
    def get_signal(self, prices, i):
        raise NotImplementedError
    
    def get_position_size(self):
        return 1.0
