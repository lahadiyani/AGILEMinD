import os
from app.memory.base_memory import MemoryStore
import faiss
import numpy as np
import json
import threading

class FaissStore(MemoryStore):
    def __init__(self, index_path, dim=768, metadata_path=None):
        self.index_path = index_path
        self.metadata_path = metadata_path or index_path + ".meta.json"
        self.dim = dim
        self.lock = threading.Lock()

        # Load FAISS index if exists
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        else:
            self.index = faiss.IndexFlatL2(dim)
        
        # Load metadata (documents)
        if os.path.exists(self.metadata_path):
            with open(self.metadata_path, "r") as f:
                self.documents = json.load(f)
        else:
            self.documents = []

    def add_documents(self, docs):
        vectors = np.array([doc['embedding'] for doc in docs], dtype='float32')
        if vectors.shape[1] != self.dim:
            raise ValueError(f"Dimensi embedding harus {self.dim}, tapi dapat {vectors.shape[1]}")

        with self.lock:
            self.index.add(vectors)
            self.documents.extend(docs)

    def similarity_search(self, query, top_k=5):
        if len(query) != self.dim:
            raise ValueError(f"Query vector harus berdimensi {self.dim}")

        with self.lock:
            D, I = self.index.search(np.array([query], dtype='float32'), top_k)
            results = []
            for idx in I[0]:
                if idx == -1 or idx >= len(self.documents):
                    continue
                results.append(self.documents[idx])
            return results

    def persist(self):
        with self.lock:
            faiss.write_index(self.index, self.index_path)
            with open(self.metadata_path, "w") as f:
                json.dump(self.documents, f)
