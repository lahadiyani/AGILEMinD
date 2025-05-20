from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, model: str = None):
        """Generate text from a prompt using the LLM."""
        pass
