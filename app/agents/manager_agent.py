from typing import List, Any
from app.agents.base_agent import BaseAgent
from app.agents.hooks_agent import pre_run_hook, post_run_hook

class AgentManager:
    def __init__(self, agents: List[BaseAgent], logging_enabled: bool = True):
        self.agents = agents
        self.logging_enabled = logging_enabled

    def log(self, message: str):
        if self.logging_enabled:
            print(f"[AgentManager] {message}")

    def run_pipeline(self, input_data: Any) -> Any:
        """
        Run the input_data through the agent pipeline, applying pre and post hooks.
        """
        self.log("Starting agent pipeline.")
        data = pre_run_hook(input_data)
        for agent in self.agents:
            self.log(f"Running agent: {agent.name}")
            data = agent.run(data)
        data = post_run_hook(data)
        self.log("Finished agent pipeline.")
        return data
