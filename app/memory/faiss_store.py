from app.memory.base import MemoryStore
import faiss
import numpy as np

class FaissStore(MemoryStore):
    def __init__(self, index_path):
        self.index_path = index_path
        try:
            self.index = faiss.read_index(index_path)
        except Exception:
            # create new index if not exists
            self.index = faiss.IndexFlatL2(768)  # dim vector (contoh)
        self.documents = []

    def add_documents(self, docs):
        # docs: list of dicts with vector embeddings
        vectors = np.array([doc['embedding'] for doc in docs]).astype('float32')
        self.index.add(vectors)
        self.documents.extend(docs)

    def similarity_search(self, query, top_k=5):
        D, I = self.index.search(np.array([query]).astype('float32'), top_k)
        results = [self.documents[i] for i in I[0]]
        return results

    def persist(self):
        faiss.write_index(self.index, self.index_path)
