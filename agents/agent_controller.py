from models.predictor import TradePredictor
from utils.logger import get_logger

class AutonomousAgent:
    def __init__(self):
        self.predictor = TradePredictor()
        self.logger = get_logger("Agent")

    def act(self):
        decision = self.predictor.predict()
        self.logger.info(f"Autonomous decision: {decision}")
        return decision



















