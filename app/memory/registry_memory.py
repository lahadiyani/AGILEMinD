from memory.base_memory import BaseMemory

class RegistryMemory:
    def __init__(self):
        self._registry = {}

    def register(self, name: str, memory: BaseMemory):
        self._registry[name] = memory

    def get(self, name: str) -> BaseMemory:
        return self._registry.get(name)

    def all(self):
        return self._registry
