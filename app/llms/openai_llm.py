from app.llms.base_llm import BaseLLM
import openai
import os

class OpenAILLM(BaseLLM):
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate(self, prompt: str, model: str = "gpt-3.5-turbo"):
        # Example for chat completion
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
