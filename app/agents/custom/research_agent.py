from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.registry import get_llm

llm = get_llm("pollinations")

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ResearcherAgent",
            description="Agent untuk melakukan penelitian berdasarkan deskripsi tugas yang diberikan.",
            prompt=PromptUtils.load_prompt("researcher_prompts.txt"),
            llm=llm,
            tools=[]
        )

    def generate_research(self, task_description: str) -> str:
        formatted_prompt = self.build_prompt(task_description)
        return self.call_llm(formatted_prompt)