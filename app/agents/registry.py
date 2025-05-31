from app.agents.base_agent import BaseAgent
from app.agents.custom.coder_agent import CoderAgent
from app.agents.custom.planner_agent import PlannerAgent
from app.agents.custom.research_agent import ResearcherAgent
from app.agents.custom.image_gen_agent import ImageGenAgent
from app.agents.custom.text_gen_agent import TextGenAgent

AGENT_REGISTRY = {
    "coder": CoderAgent,
    "planner": PlannerAgent,
    "researcher": ResearcherAgent,
    "imagegen": ImageGenAgent,
    "textgen": TextGenAgent
}

def register_agent(agent_name: str, agent_class: type):
    if not issubclass(agent_class, BaseAgent):
        raise TypeError(f"{agent_class.__name__} must subclass BaseAgent.")
    AGENT_REGISTRY[agent_name] = agent_class
