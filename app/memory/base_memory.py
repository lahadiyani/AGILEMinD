# app/memory/base_memory.py

from abc import ABC, abstractmethod
from typing import List, Any
from typing import List, Dict, Any, Optional

class MemoryStore(ABC):
    """
    Abstract base class for vector memory storage backends.
    Must support adding, searching, and persisting documents.
    """

    @abstractmethod
    def add_documents(self, docs: List[Dict[str, Any]]) -> None:
        """
        Adds documents to the memory store.

        Each document should be a dict with at least:
            - "content": the textual content
            - "metadata": dict containing metadata (source, tags, etc.)
        """
        pass

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Performs a similarity search using the query.

        Returns a list of documents like:
        [
            {
                "content": "...",
                "metadata": {...},
                "score": 0.87
            },
            ...
        ]

        `filters` is optional metadata filter (e.g., {"source": "skripsi"})
        """
        pass

    @abstractmethod
    def add_documents(self, docs: List[dict]):
        """Add documents to the vector store."""
        pass

    @abstractmethod
    def similarity_search(self, query: Any, top_k: int = 5) -> List[dict]:
        """Return top_k documents similar to the query."""

    def persist(self) -> None:
        """
        Persists memory state to disk or external storage.
        """
        pass

    @abstractmethod
    def load(self) -> None:
        """
        Loads persisted memory from storage.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Clears all stored documents. Use with caution.
        """
        pass
