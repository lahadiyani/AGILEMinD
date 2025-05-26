import os
import requests
from app.llms.base_llm import BaseLLM
from app.loaders.registry import get_loader
from config.default import Config

class PollinationsLLM(BaseLLM):
    POLLINATIONS_API_BASE_URL = Config.POLLINATIONS_API_BASE_URL
    POLLINATIONS_IMAGE_URL = Config.POLLINATIONS_IMAGE_URL
    POLLINATIONS_IMAGE_MODELS_URL = Config.POLLINATIONS_IMAGE_MODELS_URL
    POLLINATIONS_TEXT_MODELS_URL = Config.POLLINATIONS_TEXT_MODELS_URL
    
    @property
    def model_name(self):
        return "pollinations"

    def get_available_image_models(self):
        try:
            response = requests.get(self.POLLINATIONS_IMAGE_MODELS_URL)
            if response.status_code == 200:
                return response.json()
            return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_available_text_models(self):
        try:
            response = requests.get(self.POLLINATIONS_TEXT_MODELS_URL)
            if response.status_code == 200:
                return response.json()
            return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

    def generate(self, prompt: str, model: str = None):
        try:
            url = f"{self.POLLINATIONS_API_BASE_URL}/{prompt}"
            if model:
                url += f"?model={model}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"An error occurred: {e}"

    def generate_image(self, prompt: str, model: str = None):
        try:
            url = f"{self.POLLINATIONS_IMAGE_URL}/{prompt}"
            if model:
                url += f"?model={model}"
            response = requests.get(url)
            if response.status_code == 200:
                content_type = response.headers.get('content-type', '')
                if 'image' in content_type:
                    return response.content
                return f"Error: Unexpected response type: {content_type}"
            return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"
        
    def get_image_url(self, prompt: str, model: str = None) -> str:
        url = f"{self.POLLINATIONS_IMAGE_URL}/{prompt}"
        if model:
            url += f"?model={model}"
        return url
