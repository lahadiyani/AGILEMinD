from app.agents.base_agent import BaseAgent
from app.prompts.utils import load_prompt

class PlannerAgent(BaseAgent):
    def __init__(self, name="Planner", **kwargs):
        prompt = load_prompt("planner_prompts.txt")
        super().__init__(name=name, prompt=prompt, **kwargs)

    def run(self, input_text: str) -> str:
        self.log(f"Received planning task: {input_text}")
        return self.generate_plan(input_text)

    def generate_plan(self, task_description: str) -> str:
        formatted_prompt = self.prompt.replace("{input}", task_description)
        return self.call_llm(formatted_prompt)