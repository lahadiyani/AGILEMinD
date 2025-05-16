from app.agents.base_agent import BaseAgent

class CoderAgent(BaseAgent):
    def __init__(self, name="Coder"):
        super().__init__(name)

    def execute(self):
        return f"{self.name} is writing code."
