from models.predictor import PredictorAgent




class Orchestrator:
    def __init__(self, predictor):
        self.predictor = predictor

    def run_pipeline(self, raw):
        prediction = self.predictor.predict(raw)

        # Must return with correct key
        return {
            "prediction": prediction
        }