import random
import numpy as np

class TradePredictor:
    def __init__(self):
        self.state = []

    def predict(self):
        data = self._get_recent_trades()
        score = self._calculate_signal_score(data)
        return "BUY" if score > 0.5 else "SELL" if score < -0.5 else "HOLD"

    def _get_recent_trades(self):
        return np.random.randn(100)

    def _calculate_signal_score(self, trades):
        signal = np.mean(trades[-10:])
        return signal



















