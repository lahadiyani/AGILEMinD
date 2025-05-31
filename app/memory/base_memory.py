# app/memory/base_memory.py

from abc import ABC, abstractmethod
from typing import List, Any

class MemoryStore(ABC):
    """Abstract base class for vector memory stores."""

    @abstractmethod
    def add_documents(self, docs: List[dict]):
        """Add documents to the vector store."""
        pass

    @abstractmethod
    def similarity_search(self, query: Any, top_k: int = 5) -> List[dict]:
        """Return top_k documents similar to the query."""
        pass

    @abstractmethod
    def persist(self):
        """Persist memory to storage if needed."""
        pass
