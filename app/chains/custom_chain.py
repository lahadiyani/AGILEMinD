from app.chains.base_chain import BaseChain

class CustomChain(BaseChain):
    def __init__(self, agent):
        super().__init__(agent)

    def run(self):
        return f"Custom Chain is running with {self.agent.name}."
