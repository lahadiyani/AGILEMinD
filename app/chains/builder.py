# app/chain/builder.py

from app.chains.registry import CHAIN_REGISTRY
from app.agents.registry import AGENT_REGISTRY
from app.monitoring.logger import get_logger

logger = get_logger("ChainBuilder", "builder.log", component="chains")

def build_chain(config: dict):
    """
    Membangun instance chain berdasarkan konfigurasi.
    
    Args:
        config (dict): Konfigurasi chain yang minimal mengandung:
            - 'chain_name' (str): Nama chain yang akan dibangun (harus terdaftar di CHAIN_REGISTRY)
            - 'agent' (dict): Konfigurasi agent untuk chain
            - opsional parameter lain sesuai kebutuhan chain
    
    Returns:
        instance dari subclass BaseChain
    
    Raises:
        ValueError: jika konfigurasi tidak valid atau chain/agent tidak terdaftar
    """
    logger.info(f"Membangun chain dari config: {config}")

    if "chain_name" not in config:
        logger.error("Config harus mengandung 'chain_name'")
        raise ValueError("Missing 'chain_name' in chain config")

    chain_name = config["chain_name"]
    if chain_name not in CHAIN_REGISTRY:
        logger.error(f"Chain '{chain_name}' tidak terdaftar di registry")
        raise ValueError(f"Chain '{chain_name}' not registered")

    chain_class = CHAIN_REGISTRY[chain_name]

    # Ambil config agent
    agent_config = config.get("agent")
    if not agent_config:
        logger.error("Config harus mengandung konfigurasi 'agent'")
        raise ValueError("Missing 'agent' config")

    if "agent_name" not in agent_config:
        logger.error("Agent config harus mengandung 'agent_name'")
        raise ValueError("Missing 'agent_name' in agent config")

    agent_name = agent_config["agent_name"]
    if agent_name not in AGENT_REGISTRY:
        logger.error(f"Agen '{agent_name}' tidak terdaftar di registry agen")
        raise ValueError(f"Agent '{agent_name}' not registered")

    agent_class = AGENT_REGISTRY[agent_name]
    agent_params = agent_config.get("params", {})

    # Buat instance agent dengan params
    agent_instance = agent_class(**agent_params)

    # Inisialisasi chain dengan agent_instance dan parameter lain
    chain_params = config.get("chain_params", {})

    chain_instance = chain_class(agent=agent_instance, **chain_params)

    logger.info(f"Chain '{chain_name}' berhasil dibuat dengan agent '{agent_name}'")

    return chain_instance
