# elasticsearch_store.py
from app.memory.base_memory import MemoryStore
from elasticsearch import Elasticsearch

class ElasticsearchStore(MemoryStore):
    def __init__(self, host):
        self.es = Elasticsearch(hosts=[host])
        self.index_name = "vector_index"

    def add_documents(self, docs):
        # docs: list of dicts with 'embedding' and 'text'
        for i, doc in enumerate(docs):
            self.es.index(index=self.index_name, id=i, body={
                "embedding": doc["embedding"],
                "text": doc.get("text", "")
            })

    def similarity_search(self, query, top_k=5):
        # Example: cosine similarity using script_score (Elasticsearch 7+)
        script_query = {
            "size": top_k,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {"query_vector": query}
                    }
                }
            }
        }
        res = self.es.search(index=self.index_name, body=script_query)
        return [hit["_source"] for hit in res["hits"]["hits"]]

    def persist(self):
        # Elasticsearch auto-persists, nothing needed
        pass
