from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class BaseLLM(ABC):
    """
    Abstract base class for Large Language Models (LLMs).
    """

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
    def model_name(self) -> Optional[str]:
        """
        Return the name or identifier of the underlying model.
        """
        pass

    def reset(self) -> None:
        """
        Reset any internal state/context if applicable.
        Override if your LLM implementation maintains state.
        """
        pass

    async def agenerate(self, prompt: str, model: Optional[str] = None, **kwargs: Any) -> str:
        """
        Optional async method for generating text.
        Override if your LLM implementation supports async.
        """
        raise NotImplementedError("Async generation not supported.")

    def get_metadata(self) -> Dict[str, Any]:
        """
        Optional: Return metadata about the LLM (e.g., version, provider, capabilities).
        """
        return {
            "model_name": self.model_name,
            "supports_async": hasattr(self, "agenerate"),
        }
