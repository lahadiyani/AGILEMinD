# app/llms/mistral_llm.py

from app.llms.base_llm import BaseLLM
import requests
import os

class MistralLLM(BaseLLM):
    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        self.base_url = base_url or os.getenv("MISTRAL_API_URL", "https://api.mistral.ai/v1")
        
        if not self.api_key:
            raise ValueError("Mistral API key is required.")

    def generate(self, prompt: str, model: str = "mistral-tiny"):
        """
        Generate text from a prompt using the Mistral API.

        Args:
            prompt (str): The user prompt.
            model (str): The model to use (e.g., mistral-tiny, mistral-small, etc).

        Returns:
            str: The generated text response.
        """
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.RequestException as e:
            raise RuntimeError(f"Mistral API call failed: {str(e)}")
