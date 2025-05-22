from app.agents.registry import AGENT_REGISTRY
from app.agents.utils import validate_agent_config

def build_agent(config: dict):
    validate_agent_config(config)
    agent_name = config["agent_name"]
    params = config["params"]
    agent_class = AGENT_REGISTRY[agent_name]
    return agent_class(**params)
