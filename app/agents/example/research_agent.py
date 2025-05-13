from app.agents.base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    def __init__(self, name="Researcher"):
        super().__init__(name)

    def execute(self):
        return f"{self.name} is conducting research."
