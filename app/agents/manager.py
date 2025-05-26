from app.monitoring.logger import get_logger
from app.agents.base_agent import BaseAgent

logger = get_logger("AgentManager", "manager.log")

class AgentManager:
    def __init__(self, agents: list[BaseAgent]):
        self.agents = agents

    def run_pipeline(self, input_text: str) -> str:
        logger.info("Starting agent pipeline.")
        for agent in self.agents:
            logger.debug(f"Running agent: {agent.name}")
            input_text = agent.run(input_text)
        logger.info("Finished agent pipeline.")
        return input_text
