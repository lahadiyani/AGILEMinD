from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.registry import get_llm

llm = get_llm("pollinations")

class PlannerAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(
            name="PlannerAgent",
            description="Agent untuk merencanakan tugas berdasarkan deskripsi yang diberikan.",
            prompt=PromptUtils.load_prompt("planner_prompts.txt"),
            llm=llm,
            tools=[],
        )

    def generate_plan(self, task_description: str) -> str:
        formatted_prompt = self.build_prompt(task_description)  # gunakan build_prompt dari BaseAgent
        return self.call_llm(formatted_prompt)