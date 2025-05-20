from app.llms.base_llm import BaseLLM
from app.tools.pollination import generate_text, generate_image

class PollinationsLLM(BaseLLM):
    def generate(self, prompt: str, model: str = None):
        return generate_text(prompt, model)

    def generate_image(self, prompt: str, model: str = None):
        return generate_image(prompt, model)
