from app.agents.base_agent import BaseAgent
from app.agents.example.coder_agent import CoderAgent
from app.agents.example.planner_agent import PlannerAgent
from app.agents.example.research_agent import ResearcherAgent
from app.monitoring.logger import get_agent_logger

logger = get_agent_logger("AgentRegistry", "registry.log")

# example agent registry
# Daftar agen yang terdaftar
# anda bisa menambahkan agen baru ke dalam registry ini, atau anda bisa menghapusnya
AGENT_REGISTRY = {
    "CoderAgent": CoderAgent,
    "PlannerAgent": PlannerAgent,
    "ResearcherAgent": ResearcherAgent,
}

def register_agent(agent_name, agent_class):
    if not issubclass(agent_class, BaseAgent):
        logger.error(f"Gagal mendaftarkan agen: {agent_class.__name__} bukan turunan BaseAgent.")
        raise TypeError(f"{agent_class.__name__} is not a subclass of BaseAgent.")
    AGENT_REGISTRY[agent_name] = agent_class
    logger.info(f"Agen '{agent_name}' berhasil didaftarkan.")
