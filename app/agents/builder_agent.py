from app.agents.registry_agent import AGENT_REGISTRY
from app.agents.utils_agent import validate_agent_config

def build_agent(config: dict):
    """
    Build and return an agent instance from config dictionary.

    Args:
        config (dict): Configuration with keys 'agent_name' and 'params'.

    Returns:
        BaseAgent: An instance of the specified agent.
    """
    validate_agent_config(config)
    agent_name = config.get("agent_name")
    params = config.get("params", {})

    if agent_name not in AGENT_REGISTRY:
        raise ValueError(f"Agent '{agent_name}' is not registered.")

    agent_class = AGENT_REGISTRY[agent_name]
    try:
        return agent_class(**params)
    except TypeError as e:
        raise ValueError(f"Failed to instantiate agent '{agent_name}' with params {params}.") from e
