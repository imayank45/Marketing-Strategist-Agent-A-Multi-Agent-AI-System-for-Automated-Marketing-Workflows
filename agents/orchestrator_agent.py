# agents/orchestrator_agent.py
from typing import Any

class Orchestrator:
    def __init__(self, predictor, strategy_agent, evaluator, optimizer, max_iterations: int = 3, accept_threshold: float = 7.0):
        self.predictor = predictor
        self.strategy_agent = strategy_agent
        self.evaluator = evaluator
        self.optimizer = optimizer
        self.max_iterations = max_iterations
        self.accept_threshold = accept_threshold

    def run_pipeline(self, raw_inputs: dict, docs_context: str = "") -> dict:
        result = {}
        prediction = self.predictor.run(raw_inputs)
        result['prediction'] = prediction

        strategy = self.strategy_agent.generate_structured(prediction['probability'], context_summary=docs_context)
        result['initial_strategy'] = strategy

        current_strategy_text = strategy if isinstance(strategy, str) else (strategy.get('raw') or str(strategy))

        for i in range(self.max_iterations):
            eval_obj = self.evaluator.evaluate(prediction['probability'], current_strategy_text)
            result.setdefault('evaluations', []).append(eval_obj)

            if getattr(eval_obj, 'overall_score', 0) >= self.accept_threshold and not getattr(eval_obj, 'hallucination_detected', False):
                result['final_strategy'] = current_strategy_text
                result['final_evaluation'] = eval_obj
                break

            optimized = self.optimizer.optimize(current_strategy_text, eval_obj)
            result.setdefault('optimizations', []).append(optimized)
            current_strategy_text = optimized
        else:
            result['final_strategy'] = current_strategy_text
            result['final_evaluation'] = eval_obj

        return result
