from langchain_openai import ChatOpenAI

class RetrieverAgent:
    
    def __init__(self):
        
        self.llm = ChatOpenAI(
            model = "gpt-4o-mini"
        )
        
    def review(self, strategy):
        
        prompt = """
        Review this marketing startegy and provide:
        - Positive points
        - Weaknesses
        - Overall score
        Strategy:
        {strategy}
        """
        
        return self.llm.predict(prompt)