from app.chains.registry_chain import CHAIN_REGISTRY
from app.agents.builder_agent import build_agent

def build_chain(config: dict, verbose: bool = True):
    """
    Build and return a chain instance from config dictionary.

    Args:
        config (dict): Configuration with keys 'chain_name', 'agent' (or 'agents'), and optional 'chain_params'.
        verbose (bool): Whether to print debug info.

    Returns:
        BaseChain: An instance of the specified chain.
    """
    if verbose:
        print(f"[ChainBuilder] Building chain from config: {config}")

    if "chain_name" not in config:
        raise ValueError("Missing 'chain_name' in chain config")

    chain_name = config["chain_name"]
    if chain_name not in CHAIN_REGISTRY:
        raise ValueError(f"Chain '{chain_name}' not registered")

    chain_class = CHAIN_REGISTRY[chain_name]

    # Support single or multiple agents
    agent_config = config.get("agent")
    agents_config = config.get("agents")

    if agent_config:
        try:
            agents = [build_agent(agent_config)]
        except Exception as e:
            if verbose:
                print(f"[ChainBuilder] Error building agent: {str(e)}")
            raise
    elif agents_config and isinstance(agents_config, list):
        try:
            agents = [build_agent(acfg) for acfg in agents_config]
        except Exception as e:
            if verbose:
                print(f"[ChainBuilder] Error building agents: {str(e)}")
            raise
    else:
        raise ValueError("Missing 'agent' or 'agents' config")

    chain_params = config.get("chain_params", {})

    try:
        chain_instance = chain_class(agents=agents, **chain_params)
    except TypeError as e:
        if verbose:
            print(f"[ChainBuilder] Error instantiating chain '{chain_name}': {str(e)}")
        raise

    if verbose:
        agent_names = [getattr(a, 'name', str(a)) for a in agents]
        print(f"[ChainBuilder] Chain '{chain_name}' successfully created with agents {agent_names}")

    return chain_instance
