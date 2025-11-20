from models.predictor import PredictorAgent




class Orchestrator:
    def __init__(self, predictor, strategy_agent):
        self.predictor = predictor
        self.startegy_agent = strategy_agent

    def run_pipeline(self, raw):
        prediction = self.predictor.predict(raw)
        strategy = self.startegy_agent.generate_strategy(prediction["probability"])

        # Must return with correct key
        return {
            "prediction": prediction,
            "strategy": strategy
        }