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

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")
