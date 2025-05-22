import os
from app.memory.data.faiss_store import FaissStore
from app.memory.data.elasticsearch_store import ElasticsearchStore
from app.memory.data.chroma_store import ChromaStore

def get_memory_store():
    store_type = os.getenv("MEMORY_STORE_TYPE", "faiss").lower()

    if store_type == "faiss":
        index_path = os.getenv("FAISS_INDEX_PATH", "./vectorstore/index.faiss")
        return FaissStore(index_path)
    elif store_type == "elasticsearch":
        host = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")
        return ElasticsearchStore(host)
    elif store_type == "chroma":
        return ChromaStore()
    else:
        raise ValueError(f"Unknown MEMORY_STORE_TYPE: {store_type}")
