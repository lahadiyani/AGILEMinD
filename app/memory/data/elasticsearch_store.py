# app/memory/data/elasticsearch_store.py

import uuid
from app.memory.base_memory import MemoryStore
from elasticsearch import Elasticsearch, helpers

class ElasticsearchStore(MemoryStore):
    def __init__(self, host: str, dim: int = 768):
        self.es = Elasticsearch(hosts=[host])
        self.index_name = "vector_index"
        self.dim = dim
        self._ensure_index()

    def _ensure_index(self):
        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name, body={
                "mappings": {
                    "properties": {
                        "embedding": {
                            "type": "dense_vector",
                            "dims": self.dim,
                            "index": True,
                            "similarity": "cosine"
                        },
                        "text": {"type": "text"},
                        "metadata": {"type": "object"}
                    }
                }
            })

    def add_documents(self, docs):
        actions = []
        for doc in docs:
            actions.append({
                "_index": self.index_name,
                "_id": str(uuid.uuid4()),
                "_source": {
                    "embedding": doc["embedding"],
                    "text": doc.get("text", ""),
                    "metadata": doc.get("metadata", {})
                }
            })
        helpers.bulk(self.es, actions)

    def similarity_search(self, query_vector, top_k=5):
        if not isinstance(query_vector, list) or len(query_vector) != self.dim:
            raise ValueError(f"Query vector harus list dengan panjang {self.dim}")
        
        script_query = {
            "size": top_k,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {"query_vector": query_vector}
                    }
                }
            }
        }

        res = self.es.search(index=self.index_name, body=script_query)
        return [hit["_source"] for hit in res["hits"]["hits"]]

    def persist(self):
        # No-op, Elasticsearch handles persistence automatically
        pass

    def clear(self):
        """Menghapus semua dokumen di index."""
        if self.es.indices.exists(index=self.index_name):
            self.es.delete_by_query(index=self.index_name, body={"query": {"match_all": {}}})

    def load(self):
        """Mengambil semua dokumen dari index."""
        res = self.es.search(index=self.index_name, body={"query": {"match_all": {}}, "size": 1000})
        return [hit["_source"] for hit in res["hits"]["hits"]]
