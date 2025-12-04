# agents/evaluator_agent.py

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from rag.vector_store import get_vector_store
import json


class EvaluatorAgent:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.parser = StrOutputParser()
        self.vectordb = get_vector_store()

    def evaluate(self, probability: float, strategy: str) -> str:
        """
        Returns a fully structured PLAIN TEXT evaluation report.
        """

        # ----------- RAG RETRIEVAL -----------
        docs = self.vectordb.similarity_search(strategy, k=4)

        rag_context = "\n\n".join(
            [f"[SOURCE {i+1}]\n{doc.page_content}" for i, doc in enumerate(docs)]
        ) if docs else "No brand documents found."

        # ----------- MAIN EVALUATION PROMPT -----------
        prompt = f"""
You are a senior marketing strategy auditor for a bank.

Customer Subscription Probability = {probability}

Retrieved Brand / Compliance Rules:
{rag_context}

Marketing Strategy To Evaluate:
{strategy}

--------------------------------------------
STRICTLY RETURN YOUR OUTPUT IN THE FOLLOWING STRUCTURED PLAIN TEXT FORMAT:

1. PRACTICALITY CHECK
- Is this realistic for the given probability?
- Score (1–10):
- Reason:

2. ACCURACY TO PREDICTION
- Has the strategy used the probability correctly?
- Verdict (Correct / Misused):
- Explanation:

3. MARKETING QUALITY
- Clarity (1–10):
- Personalization (1–10):
- CTA Strength (1–10):
- Channel Appropriateness (1–10):
- Conversion Optimization (1–10):

4. COST & RESOURCE FEASIBILITY
- Budget Level (Low / Medium / High):
- Timeline Feasibility (Feasible / Risky):
- Explanation:

5. RAG COMPLIANCE CHECK
- Number of matching brand rules used:
- Any Budget Violation? (Yes / No):
- Any Tone Violation? (Yes / No):
- Any Compliance Risk? (Explain):

6. HALLUCINATION CHECK
- Are there claims not supported by documents? (Yes / No):
- If Yes, mention the risky claim:

7. FINAL RISK LEVEL (Low / Medium / High)

8. FINAL VERDICT
- Overall Strengths:
- Key Weaknesses:
- Should this strategy be approved? (Yes / No):
- One-line decision:

9. IMPROVEMENT SUGGESTIONS (Bullet Points)

--------------------------------------------
DO NOT return JSON.
DO NOT add extra commentary.
Return strictly in the above numbered format.
"""

        response = self.llm([HumanMessage(content=prompt)])
        structured_text = self.parser.parse(response.content)

        return structured_text
