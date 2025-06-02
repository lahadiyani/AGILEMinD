from app.chains.registry import CHAIN_REGISTRY
from app.agents.builder import build_agent
from app.monitoring.logger import get_logger

logger = get_logger("ChainBuilder", "builder.log", component="chains")

def build_chain(config: dict):
    logger.info(f"Membangun chain dari config: {config}")

    if "chain_name" not in config:
        raise ValueError("Missing 'chain_name' in chain config")

    chain_name = config["chain_name"]
    if chain_name not in CHAIN_REGISTRY:
        raise ValueError(f"Chain '{chain_name}' not registered")

    chain_class = CHAIN_REGISTRY[chain_name]

    # ✅ Gunakan builder resmi untuk agent
    agent_config = config.get("agent")
    if not agent_config:
        raise ValueError("Missing 'agent' config")

    try:
        agent_instance = build_agent(agent_config)
    except Exception as e:
        logger.error(f"Error membangun agent: {str(e)}")
        raise

    chain_params = config.get("chain_params", {})

    chain_instance = chain_class(agent=agent_instance, **chain_params)

    logger.info(f"Chain '{chain_name}' berhasil dibuat dengan agent '{agent_config.get('agent_name')}'")
    return chain_instance
