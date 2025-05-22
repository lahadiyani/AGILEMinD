from typing import Protocol, Any

class AgentTool(Protocol):
    def execute(self, input_text: str) -> str: ...

class AgentMemory(Protocol):
    def save(self, input_text: str, output_text: str) -> None: ...

class AgentLLM(Protocol):
    def generate(self, prompt: str) -> str: ...
