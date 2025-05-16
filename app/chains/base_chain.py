from app.monitoring.logger import get_logger

class BaseChain:
    def __init__(self, agents, context=None, logging_enabled=True, log_filename="base_chain.log"):
        # Pastikan agents selalu list
        self.agents = agents if isinstance(agents, list) else [agents]
        self.context = context or {}
        self.logging_enabled = logging_enabled
        
        if self.logging_enabled:
            self.logger = get_logger(self.__class__.__name__, log_filename, component="chains")
        else:
            self.logger = None
    
    def before_run(self, input_data):
        if self.logging_enabled and self.logger:
            self.logger.info(f"Starting chain with input: {input_data}")

    def after_run(self, output_data):
        if self.logging_enabled and self.logger:
            self.logger.info(f"Chain finished with output: {output_data}")

    def preprocess_input(self, input_data):
        # Override untuk manipulasi input sebelum proses agent
        return input_data

    def postprocess_output(self, output_data):
        # Override untuk manipulasi output setelah proses agent
        return output_data

    def handle_error(self, agent, error):
        if self.logging_enabled and self.logger:
            agent_name = getattr(agent, "name", repr(agent))
            self.logger.error(f"Error in agent {agent_name}: {error}", exc_info=True)
        raise error

    def run(self, input_data):
        self.before_run(input_data)
        data = self.preprocess_input(input_data)
        for agent in self.agents:
            try:
                # Pastikan run agent menerima context jika diperlukan
                if hasattr(agent.run, "__code__") and agent.run.__code__.co_argcount > 1:
                    data = agent.run(data, context=self.context)
                else:
                    data = agent.run(data)
            except Exception as e:
                self.handle_error(agent, e)
        output = self.postprocess_output(data)
        self.after_run(output)
        return output
