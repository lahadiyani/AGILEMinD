from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.registry import get_llm

llm = get_llm("pollinations")

class CoderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CoderAgent",
            description="Agent untuk menghasilkan kode berdasarkan deskripsi tugas.",
            prompt=PromptUtils.load_prompt("coder_prompts.txt"),
            llm=llm,  # cukup gunakan instance llm
            memory=None,
            tools=[],
        )

    def generate_code(self, task_description: str) -> str:
        formatted_prompt = self.build_prompt(task_description)  # gunakan build_prompt dari BaseAgent
        return self.call_llm(formatted_prompt)