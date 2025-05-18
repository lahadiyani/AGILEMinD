from abc import ABC, abstractmethod

class MemoryStore(ABC):
    """Abstract base class for vector memory stores."""

    @abstractmethod
    def add_documents(self, docs):
        """Add documents to the vector store."""
        pass

    @abstractmethod
    def similarity_search(self, query, top_k=5):
        """Return top_k documents similar to the query."""
        pass

    @abstractmethod
    def persist(self):
        """Persist memory to storage if needed."""
        pass
