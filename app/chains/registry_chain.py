from app.chains.base_chain import BaseChain
from app.agents.builder_agent import build_agent

class DynamicAgentChain(BaseChain):
    """
    A chain that dynamically builds and executes multiple agents based on configuration.
    """

    def __init__(self, agent_configs: list, verbose: bool = True):
        """
        Args:
            agent_configs (list): A list of dicts, each representing an agent config.
            verbose (bool): If True, print info when loading agents.
        """
        agents = []
        for config in agent_configs:
            agent_instance = build_agent(config)
            if verbose:
                print(f"[DynamicAgentChain] Loaded agent: {getattr(agent_instance, 'name', agent_instance.__class__.__name__)}")
            agents.append(agent_instance)
        super().__init__(agents=agents)
        self.verbose = verbose

    def run(self, input_data):
        """
        Run input data sequentially through all agents in the chain.
        """
        result = input_data
        for agent in self.agents:
            result = agent.run(result)  # Chain execution from one agent to the next
        return result
