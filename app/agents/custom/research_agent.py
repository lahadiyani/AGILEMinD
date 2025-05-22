from app.agents.base_agent import BaseAgent
from app.prompts.utils import load_prompt

class ResearcherAgent(BaseAgent):
    def __init__(self, name="Researcher", **kwargs):
        prompt = load_prompt("researcher_prompts.txt")  # File prompt khusus researcher
        super().__init__(name=name, prompt=prompt, **kwargs)

    def run(self, input_text: str) -> str:
        self.log(f"Received research task: {input_text}")
        return self.generate_research(input_text)

    def generate_research(self, task_description: str) -> str:
        formatted_prompt = self.prompt.replace("{input}", task_description)
        return self.call_llm(formatted_prompt)