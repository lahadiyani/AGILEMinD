from app.agents.registry import AGENT_REGISTRY
from app.monitoring.logger import get_logger

logger = get_logger("AgentUtils", "utils.log")

def validate_agent_config(config: dict) -> bool:
    required_keys = ["agent_name", "params"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"{key} missing in agent config")

    if config["agent_name"] not in AGENT_REGISTRY:
        raise ValueError(f"Agent '{config['agent_name']}' not registered.")

    if not isinstance(config["params"], dict):
        raise TypeError("'params' must be a dictionary.")

    logger.info(f"Validated config for agent: {config['agent_name']}")
    return True
