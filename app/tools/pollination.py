import requests
import os
from flask import current_app

POLLINATIONS_API_BASE_URL = os.getenv("POLLINATIONS_API_BASE_URL", "https://text.pollinations.ai")
POLLINATIONS_IMAGE_URL = os.getenv("POLLINATIONS_IMAGE_URL", "https://image.pollinations.ai/prompt")
POLLINATIONS_IMAGE_MODELS_URL = os.getenv("POLLINATIONS_IMAGE_MODELS_URL", "https://image.pollinations.ai/models")
POLLINATIONS_TEXT_MODELS_URL = os.getenv("POLLINATIONS_TEXT_MODELS_URL", "https://text.pollinations.ai/models")

def get_available_image_models():
    """Get available image generation models from Pollinations.AI"""
    try:
        response = requests.get(POLLINATIONS_IMAGE_MODELS_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_text_models():
    """Get available text generation models from Pollinations.AI"""
    try:
        response = requests.get(POLLINATIONS_TEXT_MODELS_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

def generate_text(prompt: str, model: str = None):
    """Generasi teks dari Pollinations.AI"""
    try:
        url = f"{POLLINATIONS_API_BASE_URL}/{prompt}"
        if model:
            url += f"?model={model}"
            
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"

def generate_image(prompt: str, model: str = None):
    """Generasi gambar dari Pollinations.AI"""
    try:
        url = f"{POLLINATIONS_IMAGE_URL}/{prompt}"
        if model:
            url += f"?model={model}"
            
        response = requests.get(url)
        if response.status_code == 200:
            # Check if the response is actually an image
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type:
                return response.content
            else:
                return f"Error: Unexpected response type: {content_type}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
