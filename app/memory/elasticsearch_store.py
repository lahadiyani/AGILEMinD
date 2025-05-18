# elasticsearch_store.py
from app.memory.base import MemoryStore
from elasticsearch import Elasticsearch

class ElasticsearchStore(MemoryStore):
    def __init__(self, host):
        self.es = Elasticsearch(hosts=[host])
        self.index_name = "vector_index"

    def add_documents(self, docs):
        # Implement indexing dokumen ke Elasticsearch
        pass

    def similarity_search(self, query, top_k=5):
        # Implement query similarity search ke Elasticsearch
        pass

    def persist(self):
        # Biasanya tidak perlu karena langsung tersimpan
        pass
