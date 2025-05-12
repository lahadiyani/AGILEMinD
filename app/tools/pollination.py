import requests
import os

POLLINATIONS_API_BASE_URL = os.getenv("POLLINATIONS_API_BASE_URL", "https://text.pollinations.ai")
POLLINATIONS_IMAGE_URL = os.getenv("POLLINATIONS_IMAGE_URL", "https://image.pollinations.ai/prompt")

def generate_text(prompt: str):
    """Generasi teks dari Pollinations.AI"""
    try:
        response = requests.get(f"{POLLINATIONS_API_BASE_URL}/{prompt}")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"

def generate_image(prompt: str):
    """Generasi gambar dari Pollinations.AI"""
    try:
        response = requests.get(f"{POLLINATIONS_IMAGE_URL}/{prompt}")
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
