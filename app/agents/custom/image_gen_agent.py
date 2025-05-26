from app.agents.base_agent import BaseAgent
from app.prompts.utils import PromptUtils
from app.llms.registry import get_llm
from app.loaders.registry import get_loader
from urllib.parse import quote_plus

llm = get_llm("pollinations")
load = get_loader("ImageLoader")

class ImageGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ImageGenAgent",
            description="Agent untuk menghasilkan gambar berdasarkan deskripsi.",
            prompt=PromptUtils.load_prompt("image_gen_prompts.txt"),
            llm=llm,
            memory=None,
            tools=[],
        )
        self.image_loader = load(save_dir="app/static/output/image/")

    def run(self, prompt, model=None):
        image_url = self.generate_image(prompt)
        docs = self.image_loader.load(image_url)
        image_path = docs[0]["content"] if docs else None
        return {
            "image_path": image_path,
            "image_description": prompt,
            "model": model or self.llm.model_name,
        }

    def generate_image(self, image_description: str) -> str:
        formatted_prompt = self.build_prompt(image_description)
        encoded_prompt = quote_plus(formatted_prompt)
        image_url = self.llm.get_image_url(encoded_prompt)
        if not image_url:
            raise ValueError("Failed to generate image URL.")
        return image_url

    def get_available_image_models(self):
        model = self.llm.get_available_image_models()
        return model if isinstance(model, list) else [model]