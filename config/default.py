import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.urandom(24)
    DEBUG = False
    ENV = 'production'

    # Ini bagian penting:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MEMORY_STORE_TYPE=os.getenv("MEMORY_STORE_TYPE", "faiss").lower()
    FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "./vectorstore/index.faiss")

    POLLINATIONS_API_BASE_URL = os.getenv("POLLINATIONS_API_BASE_URL", "https://text.pollinations.ai")
    POLLINATIONS_IMAGE_URL = os.getenv("POLLINATIONS_IMAGE_URL", "https://image.pollinations.ai/prompt")
    POLLINATIONS_IMAGE_MODELS_URL = os.getenv("POLLINATIONS_IMAGE_MODELS_URL", "https://image.pollinations.ai/models")
    POLLINATIONS_TEXT_MODELS_URL = os.getenv("POLLINATIONS_TEXT_MODELS_URL", "https://text.pollinations.ai/models")

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")
