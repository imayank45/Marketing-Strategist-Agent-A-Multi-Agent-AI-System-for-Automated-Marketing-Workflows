from langchain_openai import ChatOpenAI

class StrategyAgent:
    
    def __init__(self):
        
        self.llm =  ChatOpenAI(
            model = "gpt-4o-mini",
            temperature=0.4
        )
    
    def generate_strategy(self, prediciton):
        
        prompt = """
        You are a bank marketing expert.
        Based on subscription probability {prediction},
        generate a detailed market strategy with:
         - Channel selection
         - Budget split
         - High-probability customer segments
         - Message plan
        """
        
        return self.llm.predict(prompt)