from app.llms.pollinations_llm import PollinationsLLM
from app.llms.openai_llm import OpenAILLM

LLM_REGISTRY = {
    "pollinations": PollinationsLLM,
    "openai": OpenAILLM,
}

def get_llm(llm_name: str, **kwargs):
    if llm_name not in LLM_REGISTRY:
        raise ValueError(f"LLM '{llm_name}' not registered.")
    return LLM_REGISTRY[llm_name](**kwargs)
