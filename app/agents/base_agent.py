class BaseAgent:
    def __init__(self, name):
        self.name = name

    def execute(self):
        raise NotImplementedError("Method 'execute' must be implemented.")