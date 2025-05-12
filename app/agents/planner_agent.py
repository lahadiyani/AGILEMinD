from app.agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self, name="Planner"):
        super().__init__(name)

    def execute(self):
        return f"{self.name} is planning tasks."
