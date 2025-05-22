from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, Union

class BaseLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str, model: Optional[str] = None, **kwargs: Any) -> str:
        """
        Generate text from a prompt using the LLM.

        Args:
            prompt (str): The input prompt.
            model (Optional[str]): Model identifier or name.
            **kwargs: Additional model-specific generation parameters like temperature, max_tokens, etc.

        Returns:
            str: Generated text output from the model.

        Raises:
            Exception: Define specific exceptions or use a base LLM exception.
        """
        pass

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Return the name or identifier of the underlying model."""
        pass

    def reset(self):
        """Reset any internal state/context if applicable."""
        pass

    # Optional async method, jika framework mendukung
    async def agenerate(self, prompt: str, model: Optional[str] = None, **kwargs: Any) -> str:
        raise NotImplementedError("Async generation not supported.")
