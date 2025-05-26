from typing import Type
from app.llms.base_llm import BaseLLM
from app.llms.pollinations_llm import PollinationsLLM
from app.llms.openai_llm import OpenAILLM
from app.llms.mistral_llm import MistralLLM

LLM_REGISTRY: dict[str, Type[BaseLLM]] = {
    "pollinations": PollinationsLLM,
    "openai": OpenAILLM,
    "mistral": MistralLLM,
}

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
