class Orchestrator:
    def __init__(self, predictor, strategy_agent, reviewer, optimizer):
        self.predictor = predictor
        self.strategy_agent = strategy_agent
        self.reviewer = reviewer
        self.optimizer = optimizer

    def run_pipeline(self, raw):
        # Step 1: Prediction
        prediction = self.predictor.predict(raw)

        # Step 2: Strategy generation
        strategy = self.strategy_agent.generate_strategy(prediction["probability"])

        # Step 3: Review (only one parameter)
        review = self.reviewer.review(strategy)

        # Step 4: Optimization
        optimized = self.optimizer.optimize(strategy, review)

        # Final response
        return {
            "prediction": prediction,
            "strategy": strategy,
            "review": review,
            "optimized_strategy": optimized
        }
