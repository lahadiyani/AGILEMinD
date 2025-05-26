from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.registry import get_llm

llm = get_llm("pollinations")
class TextGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TextGenAgent",
            description="Agent untuk menghasilkan teks berdasarkan deskripsi.",
            prompt=PromptUtils.load_prompt("text_gen_prompts.txt"),
            llm=llm,  # cukup gunakan instance llm
            memory=None,
            tools=[],
        )

    def generate_image(self, image_description: str) -> str:
        formatted_prompt = self.build_prompt(image_description)  # gunakan build_prompt dari BaseAgent
        return self.call_llm(formatted_prompt)
    
    def get_available_text_models(self):
        return self.llm.get_available_text_models()