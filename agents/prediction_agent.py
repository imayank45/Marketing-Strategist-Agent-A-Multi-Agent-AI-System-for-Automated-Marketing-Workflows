# agents/prediction_agent.py
from models.predictor import PredictorAgent
from typing import List

class PredictionAgent:
    def __init__(self, model_path: str, feature_order: List[str]):
        self.predictor = PredictorAgent(model_path, feature_order)

    def run(self, raw_inputs: dict) -> dict:
        return self.predictor.predict(raw_inputs)
