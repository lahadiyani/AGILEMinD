from typing import Any, List, Optional, Dict

class BaseChain:
    """
    Base class for chaining multiple agents in a pipeline.
    """

    def __init__(
        self,
        agents: List[Any],
        context: Optional[Dict] = None,
        logging_enabled: bool = True,
    ):
        self.agents = agents if isinstance(agents, list) else [agents]
        self.context = context or {}
        self.logging_enabled = logging_enabled

    def log(self, message: str) -> None:
        if self.logging_enabled:
            print(f"[{self.__class__.__name__}] {message}")

    def before_run(self, input_data: Any) -> None:
        self.log(f"Starting chain with input: {input_data}")

    def after_run(self, output_data: Any) -> None:
        self.log(f"Chain finished with output: {output_data}")

    def preprocess_input(self, input_data: Any) -> Any:
        return input_data

    def postprocess_output(self, output_data: Any) -> Any:
        return output_data

    def handle_error(self, agent: Any, error: Exception) -> None:
        agent_name = getattr(agent, "name", repr(agent))
        self.log(f"Error in agent {agent_name}: {str(error)}")
        raise error

    def run(self, input_data: Any) -> Any:
        self.before_run(input_data)
        data = self.preprocess_input(input_data)
        for agent in self.agents:
            try:
                self.log(f"Running agent: {agent.__class__.__name__}")
                data = agent.run(data)
            except Exception as e:
                self.handle_error(agent, e)
        output = self.postprocess_output(data)
        self.after_run(output)
        return output
