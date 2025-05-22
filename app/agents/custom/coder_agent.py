from app.agents.base_agent import BaseAgent
from app.prompts.utils import load_prompt

class CoderAgent(BaseAgent):
    def __init__(self, name="Coder", **kwargs):
        prompt = load_prompt("coder_prompts.txt")
        super().__init__(name=name, prompt=prompt, **kwargs)

    def run(self, input_text: str) -> str:
        self.log(f"Received coding task: {input_text}")
        return self.generate_code(input_text)

    def generate_code(self, task_description: str) -> str:
        formatted_prompt = self.prompt.replace("{input}", task_description)
        return self.call_llm(formatted_prompt)
