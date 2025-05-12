class BaseChain:
    def __init__(self, agent):
        self.agent = agent

    def run(self):
        raise NotImplementedError("Method 'run' must be implemented.")
