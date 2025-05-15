import time
import logging
from models.predictor import TradePredictor
from utils.logger import get_logger

class TradingEngine:
    def __init__(self):
        self.predictor = TradePredictor()
        self.logger = get_logger("TradingEngine")

    def run(self):
        self.logger.info("Engine started.")
        while True:
            try:
                signal = self.predictor.predict()
                self.execute_trade(signal)
                time.sleep(5)
            except Exception as e:
                self.logger.error(f"Engine error: {e}")

    def execute_trade(self, signal):
        if signal == "BUY":
            self.logger.info("Executing BUY")
        elif signal == "SELL":
            self.logger.info("Executing SELL")
        else:
            self.logger.info("Holding position")

if __name__ == "__main__":
    engine = TradingEngine()
    engine.run()



















