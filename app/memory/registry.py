# app/memory/registry.py

from app.memory.data.pgvector_store import PGVectorStore
from app.memory.data.chroma_store import ChromaStore
from app.memory.data.faiss_store import FaissStore
from app.memory.data.elasticsearch_store import ElasticsearchStore

MEMORY_STORE_REGISTRY = {
    "pgvector": PGVectorStore,
    "chroma": ChromaStore,
    "faiss": FaissStore,
    "elasticsearch": ElasticsearchStore
}
