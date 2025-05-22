from app.llms.base_llm import BaseLLM
import openai
import os
from typing import Optional, Any

class OpenAILLM(BaseLLM):
    def __init__(self, api_key: Optional[str] = None, default_model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.default_model = default_model
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided")
        # Jangan set openai.api_key secara global

    def generate(self, prompt: str, model: Optional[str] = None, **kwargs: Any) -> str:
        """
        Generate text from prompt using OpenAI chat completion.

        Args:
            prompt (str): User input prompt.
            model (Optional[str]): Model name, defaults to default_model.
            **kwargs: Additional parameters for OpenAI API.

        Returns:
            str: Generated text.
        """
        model = model or self.default_model
        try:
            response = openai.ChatCompletion.create(
                api_key=self.api_key,
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            # Bisa custom exception handling/logging
            raise RuntimeError(f"OpenAI API call failed: {e}") from e
