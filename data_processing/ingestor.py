import random
import json
import datetime

class DataIngestor:
    def __init__(self):
        self.database = []

    def ingest(self):
        mock_trade = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "volume": random.uniform(0.1, 10.0),
            "price": random.uniform(1.0, 200.0)
        }
        self.database.append(mock_trade)
        return mock_trade

    def save_to_disk(self, path="/tmp/data.json"):
        with open(path, "w") as f:
            json.dump(self.database, f)



















