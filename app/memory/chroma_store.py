# app/memory/chroma_store.py

from app.memory.base_memory import MemoryStore

class ChromaStore(MemoryStore):
    def __init__(self):
        # Inisialisasi chroma vector store (dummy)
        self.documents = []

    def add_documents(self, docs):
        self.documents.extend(docs)

    def similarity_search(self, query, top_k=5):
        # Dummy: return first top_k docs
        return self.documents[:top_k]

    def persist(self):
        # Implement persistence if needed
        pass
