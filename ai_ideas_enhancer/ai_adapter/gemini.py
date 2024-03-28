from . import BaseGenAIAdapter
from google.generativeai import GenerativeModel

class GeminiAdapter(BaseGenAIAdapter):
    def __init__(self, model: GenerativeModel) -> None:
        self.model = model
        
    def generate(self, prompt: str) -> str:
        return self.model.generate_content(prompt).text
