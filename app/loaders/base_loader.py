#app/loaders/base_loader.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any, TypedDict, Union
import os

class LoaderException(Exception):
    """Custom exception for loader errors."""
    pass

class Document(TypedDict):
    content: str
    metadata: Dict[str, Any]

class BaseLoader(ABC):
    """
    Abstract base class for all document/data loaders.
    """

    @abstractmethod
    def load(self, source: Union[str, os.PathLike], **kwargs) -> List[Document]:
        """
        Load data from the given source and return a list of Document objects.

        Args:
            source (Union[str, os.PathLike]): Path, URL, or identifier of the data source.
            **kwargs: Optional parameters like encoding, headers, etc.

        Returns:
            List[Document]: List of loaded documents with content and metadata.

        Raises:
            LoaderException: If the loader fails to load or parse the source.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def load_all(self, sources: List[Union[str, os.PathLike]], **kwargs) -> List[Document]:
        """
        Load multiple sources and aggregate documents.

        Args:
            sources (List[Union[str, os.PathLike]]): List of data sources.

        Returns:
            List[Document]: Aggregated list of documents from all sources.
        """
        results = []
        for src in sources:
            try:
                docs = self.load(src, **kwargs)
                results.extend(docs)
            except Exception as e:
                raise LoaderException(f"Failed to load source '{src}': {e}") from e
        return results
