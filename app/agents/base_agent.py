from abc import ABC, abstractmethod
from typing import Optional, List, Any, Dict
from app.agents.types_agent import AgentTool, AgentMemory, AgentLLM

class BaseAgent(ABC):
    """
    Abstract base class for AI agents.
    """

    def __init__(
        self,
        name: str,
        description: Optional[str] = "",
        prompt: Optional[str] = None,
        llm: Optional[AgentLLM] = None,
        memory: Optional[AgentMemory] = None,
        tools: Optional[List[AgentTool]] = None,
        models: Optional[List[str]] = None,
        logging_enabled: bool = True
    ):
        self.name = name
        self.description = description
        self.prompt = prompt
        self.llm = llm
        self.models = models if models else (llm.model_name if llm else None)
        self.memory = memory
        self.tools = tools or []
        self.logging_enabled = logging_enabled

    def log(self, message: str):
        if self.logging_enabled:
            print(f"[{self.__class__.__name__}][{self.name}] {message}")

    def validate(self):
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        if not self.llm:
            raise ValueError("LLM instance not configured.")

    def build_prompt(self, **kwargs) -> str:
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        try:
            return self.prompt.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing prompt variable: {e}")

    def call_llm(self, prompt: str, model: Optional[str] = None) -> str:
        self.log(f"Calling LLM with prompt: {prompt}" + (f" and model: {model}" if model else ""))
        return self.llm.generate(prompt, model=model) if model else self.llm.generate(prompt)

    def preprocess(self, input_data: Any) -> Dict:
        return {"input": input_data} if isinstance(input_data, str) else input_data

    def postprocess(self, response: Any) -> Any:
        self.log(f"Raw response: {response}")
        return response

    def remember(self, input_text: str, output_text: str):
        if self.memory:
            self.memory.save(input_text, output_text)
            self.log("Saved to memory.")

    def use_tools(self, tool_name: str, *args, **kwargs) -> Any:
        for tool in self.tools:
            if tool.name == tool_name:
                self.log(f"Using tool: {tool_name}")
                return tool.run(*args, **kwargs)
        raise ValueError(f"Tool '{tool_name}' not found.")

    def run(self, input_data: Any, model: Optional[str] = None) -> Any:
        try:
            self.validate()
            preprocessed = self.preprocess(input_data)
            self.log(f"Input: {preprocessed}" + (f", Model: {model}" if model else ""))
            prompt = self.build_prompt(**preprocessed)
            result = self.call_llm(prompt, model=model)
            self.remember(str(input_data), result)
            return self.postprocess(result)
        except Exception as e:
            self.log(f"Error occurred: {e}")
            raise
