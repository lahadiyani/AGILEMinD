from app.monitoring.logger import get_agent_logger

class BaseAgent:
    """
    Kelas dasar untuk semua agen dalam sistem.
    """

    def __init__(self, name, description=None, prompt=None, llm=None, memory=None, tools=None, logging_enabled=True):
        self.name = name
        self.description = description or ""
        self.prompt = prompt
        self.llm = llm
        self.memory = memory
        self.tools = tools or []
        self.logging_enabled = logging_enabled

        # Inisialisasi logger
        if self.logging_enabled:
            log_filename = f"{self.name.lower()}_agent.log"
            self.logger = get_agent_logger(f"{self.__class__.__name__}.{self.name}", log_filename)
        else:
            self.logger = None

    def log(self, message):
        """Log pesan jika logging diaktifkan."""
        if self.logger:
            self.logger.info(f"[{self.name}] {message}")

    def validate(self):
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        if not self.llm:
            raise ValueError("LLM instance not configured.")

    def build_prompt(self, input_text):
        if not self.prompt:
            raise ValueError("Prompt not configured.")
        return self.prompt.replace("{input}", input_text)

    def call_llm(self, prompt):
        if not self.llm:
            raise ValueError("LLM instance not configured.")
        self.log(f"Calling LLM with prompt: {prompt}")
        return self.llm.generate(prompt)

    def postprocess(self, response):
        self.log(f"Raw response from LLM: {response}")
        return response  # Bisa di-custom

    def remember(self, input_text, output_text):
        if self.memory:
            self.memory.save(input_text, output_text)
            self.log("Interaction saved in memory.")

    def run(self, input_text):
        try:
            self.validate()
            self.log(f"Running agent with input: {input_text}")
            prompt = self.build_prompt(input_text)
            response = self.call_llm(prompt)
            self.remember(input_text, response)
            return self.postprocess(response)
        except Exception as e:
            if self.logger:
                self.logger.error(f"Error occurred: {e}", exc_info=True)
            raise
