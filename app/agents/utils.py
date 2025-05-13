from app.agents.registry import AGENT_REGISTRY
from app.monitoring.logger import get_agent_logger

logger = get_agent_logger("AgentUtils", "utils.log")

def validate_agent_config(config):
    logger.debug(f"Validasi konfigurasi agen: {config}")
    required_keys = ["agent_name", "params"]

    for key in required_keys:
        if key not in config:
            logger.error(f"Konfigurasi agen tidak valid. Key '{key}' hilang.")
            raise ValueError(f"{key} missing in agent config")

    agent_name = config["agent_name"]
    if agent_name not in AGENT_REGISTRY:
        logger.error(f"Agen '{agent_name}' tidak terdaftar dalam registry.")
        raise ValueError(f"Agent '{agent_name}' not registered.")

    if not isinstance(config["params"], dict):
        logger.error(f"Parameter untuk agen '{agent_name}' bukan dictionary.")
        raise TypeError("'params' must be a dictionary.")

    logger.info(f"Konfigurasi agen '{agent_name}' valid.")
    return True
