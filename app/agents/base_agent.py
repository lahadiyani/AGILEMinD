from abc import ABC, abstractmethod
from app.monitoring.logger import get_logger
from typing import Optional, List, Any
from app.agents.types import AgentTool, AgentMemory, AgentLLM

class BaseAgent(ABC):
    def __init__(self,
                 name: str,
                 description: Optional[str] = "",
                 prompt: Optional[str] = None,
                 llm: Optional[AgentLLM] = None,
                 memory: Optional[AgentMemory] = None,
                 tools: Optional[List[AgentTool]] = None,
                 models: Optional[List[str]] = None,
                 logging_enabled: bool = True):

        self.name = name
        self.description = description
        self.prompt = prompt
        self.llm = llm
        self.models = llm.model_name if llm else None
        self.memory = memory
        self.tools = tools or []
        self.logging_enabled = logging_enabled

        self.logger = get_logger(f"{self.__class__.__name__}.{self.name}", f"{self.name.lower()}_agent.log") if logging_enabled else None

    def log(self, message: str):
        if self.logger:
            self.logger.info(f"[{self.name}] {message}")

    def validate(self):
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        if not self.llm:
            raise ValueError("LLM instance not configured.")

    def build_prompt(self, input_text: str) -> str:
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        return self.prompt.replace("{input}", input_text)

    def call_llm(self, prompt: str, model: str = None) -> str:
        self.log(f"Calling LLM with prompt: {prompt}" + (f" and model: {model}" if model else ""))
        if model:
            return self.llm.generate(prompt, model=model)
        return self.llm.generate(prompt)

    def postprocess(self, response: Any) -> Any:
        self.log(f"Raw response: {response}")
        return response

    def remember(self, input_text: str, output_text: str):
        if self.memory:
            self.memory.save(input_text, output_text)
            self.log("Saved to memory.")

    def run(self, input_text: str, model: str = None) -> Any:
        try:
            self.validate()
            self.log(f"Input: {input_text}" + (f", Model: {model}" if model else ""))
            prompt = self.build_prompt(input_text)
            result = self.call_llm(prompt, model=model)
            self.remember(input_text, result)
            return self.postprocess(result)
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error occurred: {e}", exc_info=True)
            raise
