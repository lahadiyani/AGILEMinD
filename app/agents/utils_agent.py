from app.agents.registry_agent import AGENT_REGISTRY
from typing import Dict, Any

def validate_agent_config(config: Dict[str, Any], verbose: bool = True) -> bool:
    """
    Validate the agent configuration dictionary.

    Args:
        config (Dict[str, Any]): Configuration with 'agent_name' and 'params'.
        verbose (bool): Whether to print validation status.

    Returns:
        bool: True if config is valid, raises ValueError/TypeError otherwise.
    """
    required_keys = ["agent_name", "params"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"'{key}' missing in agent config.")

    agent_name = config["agent_name"]
    params = config["params"]

    if not isinstance(agent_name, str) or not agent_name:
        raise TypeError("'agent_name' must be a non-empty string.")

    if agent_name not in AGENT_REGISTRY:
        raise ValueError(f"Agent '{agent_name}' not registered.")

    if not isinstance(params, dict):
        raise TypeError("'params' must be a dictionary.")

    if verbose:
        print(f"[AgentUtils] Validated config for agent: {agent_name}")
    return True
