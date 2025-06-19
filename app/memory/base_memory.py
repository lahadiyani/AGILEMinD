from abc import ABC, abstractmethod
from typing import Any, List, Tuple

class BaseMemory(ABC):
    @abstractmethod
    def add(self, role: str, content: str, metadata: dict) -> None:
        pass

    @abstractmethod
    def retrieve(self, query: str, limit: int = 10) -> List[Tuple[str, str, dict]]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
