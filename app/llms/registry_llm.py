from typing import Type, Dict
from app.llms.base_llm import BaseLLM
from app.llms.custom.pollinations_llm import PollinationsLLM
from app.llms.custom.openai_llm import OpenAILLM
from app.llms.custom.mistral_llm import MistralLLM

LLM_REGISTRY: Dict[str, Type[BaseLLM]] = {
    "pollinations": PollinationsLLM,
    "openai": OpenAILLM,
    "mistral": MistralLLM,
}

def register_llm(llm_name: str, llm_class: Type[BaseLLM]) -> None:
    """
    Register a new LLM class to the registry.

    Args:
        llm_name (str): The name to register the LLM under.
        llm_class (Type[BaseLLM]): The LLM class to register.

    Raises:
        TypeError: If llm_class is not a subclass of BaseLLM.
    """
    if not issubclass(llm_class, BaseLLM):
        raise TypeError(f"{llm_class.__name__} must subclass BaseLLM.")
    LLM_REGISTRY[llm_name] = llm_class

def get_llm(llm_name: str, **kwargs) -> BaseLLM:
    """
    Retrieve an instance of a registered LLM by name.

    Args:
        llm_name (str): The key name of the LLM to instantiate.
        **kwargs: Arguments to pass to the LLM constructor.

    Returns:
        BaseLLM: Instance of the requested LLM.

    Raises:
        ValueError: If the requested LLM is not registered.
    """
    try:
        llm_class = LLM_REGISTRY[llm_name]
    except KeyError:
        available = ", ".join(LLM_REGISTRY.keys())
        raise ValueError(f"LLM '{llm_name}' not registered. Available: {available}")
    return llm_class(**kwargs)
