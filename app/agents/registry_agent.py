from app.agents.base_agent import BaseAgent
from app.agents.custom.coder_agent import CoderAgent
from app.agents.custom.planner_agent import PlannerAgent
from app.agents.custom.research_agent import ResearcherAgent
from app.agents.custom.image_gen_agent import ImageGenAgent
from app.agents.custom.text_gen_agent import TextGenAgent
from typing import Type, Dict

AGENT_REGISTRY: Dict[str, Type[BaseAgent]] = {
    "coder": CoderAgent,
    "planner": PlannerAgent,
    "researcher": ResearcherAgent,
    "imagegen": ImageGenAgent,
    "textgen": TextGenAgent
}

def register_agent(agent_name: str, agent_class: Type[BaseAgent]) -> None:
    """
    Register a new agent class to the registry.

    Args:
        agent_name (str): The name to register the agent under.
        agent_class (Type[BaseAgent]): The agent class to register.

    Raises:
        TypeError: If agent_class is not a subclass of BaseAgent.
    """
    if not issubclass(agent_class, BaseAgent):
        raise TypeError(f"{agent_class.__name__} must subclass BaseAgent.")
    AGENT_REGISTRY[agent_name] = agent_class
