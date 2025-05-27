
import os
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from app.memory.base_memory import MemoryStore

class ChromaStore(MemoryStore):
    def __init__(self, persist_directory: str = "chroma_data"):
        self.persist_directory = persist_directory
        self.client = chromadb.Client(
            chromadb.config.Settings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=self.persist_directory
            )
        )

        self.embedding_function = OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"))
        self.collection = self.client.get_or_create_collection(
            name="rag_documents",
            embedding_function=self.embedding_function
        )

    def add_documents(self, docs):
        ids = [str(i) for i in range(len(docs))]
        contents = [doc["content"] for doc in docs]
        metadatas = [doc.get("metadata", {}) for doc in docs]

        self.collection.add(
            documents=contents,
            ids=ids,
            metadatas=metadatas
        )

    def similarity_search(self, query, top_k=5):
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        return [
            {"content": doc, "metadata": meta}
            for doc, meta in zip(documents, metadatas)
        ]

    def persist(self):
        self.client.persist()
