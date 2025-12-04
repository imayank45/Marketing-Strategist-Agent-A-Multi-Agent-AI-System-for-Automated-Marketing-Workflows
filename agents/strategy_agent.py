# agents/strategy_agent.py
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import json
from utils.prompts import STRATEGY_PROMPT

class StrategyAgent:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

    def generate(self, probability: float, context_summary: str = "") -> str:
        prompt = STRATEGY_PROMPT + "\nContext summary:\n" + (context_summary or "No additional context.")
        filled = prompt.format(probability=probability)
        res = self.llm([HumanMessage(content=filled)])
        return res.content

    def generate_structured(self, probability: float, context_summary: str = "") -> dict:
        raw = self.generate(probability, context_summary)
        try:
            return json.loads(raw)
        except Exception:
            return {"raw": raw}
