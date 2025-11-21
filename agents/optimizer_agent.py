from langchain_openai import ChatOpenAI

class OptimizerAgent:
    
    def __init__(self):
        
        self.llm = ChatOpenAI(
            model = "gpt-4o-mini"
        )
        
        
    def optimize(self, strategy, review):
        
        prompt = f"""
        Improve this marketing strategy based on review feedback.
        
        Strategy:
        {strategy}
        
        Review:
        {review}
        
        Generate a corrected, optimized, high-impact bank campaign plan.
        """
        
        return self.llm.predict(prompt)