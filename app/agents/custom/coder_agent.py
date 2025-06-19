from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.builder_llm import BuilderLLM

class CoderAgent(BaseAgent):
    def __init__(self, prompt_file: str = "coder_prompts.txt", llm_name: str = "pollinations", **kwargs):
        super().__init__(
            name="CoderAgent",
            description="Agent untuk menghasilkan kode berdasarkan deskripsi tugas.",
            prompt=PromptUtils.load_prompt(prompt_file),
            llm=BuilderLLM.build_llm({'llm_name': llm_name}),
            memory=kwargs.get("memory"),
            tools=kwargs.get("tools", []),
        )

    def generate_code(self, task_description: str) -> str:
        formatted_prompt = self.build_prompt(task_description)
        return self.call_llm(formatted_prompt)