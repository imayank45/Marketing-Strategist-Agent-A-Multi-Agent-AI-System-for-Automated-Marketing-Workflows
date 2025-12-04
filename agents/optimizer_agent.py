# agents/optimizer_agent.py
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import json

class OptimizerAgent:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.2):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

    def optimize(self, strategy: str, evaluation) -> str:
        eval_text = evaluation.json() if hasattr(evaluation, 'json') else json.dumps(evaluation)
        prompt = (
            "Improve the strategy based on this evaluation and produce an optimized strategy.\n\n"
            f"EVALUATION:\n{eval_text}\n\nSTRATEGY:\n{strategy}\n\n"
            "Return a finalized, actionable campaign plan with clear budgets, timeline and CTAs."
        )
        resp = self.llm([HumanMessage(content=prompt)])
        return resp.content
