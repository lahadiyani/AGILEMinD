from app.monitoring.logger import get_agent_logger

logger = get_agent_logger("AgentManager", "manager.log")

class AgentManager:
    """
    Mengelola dan menjalankan pipeline dari beberapa agen secara berurutan.
    """

    def __init__(self, agents=None):
        self.agents = agents or []
        logger.info("AgentManager diinisialisasi dengan agen-agen.")

    def run_pipeline(self, input_text):
        logger.info("Pipeline agen dimulai.")
        try:
            for agent in self.agents:
                logger.debug(f"Menjalankan agen '{agent.name}'")
                input_text = agent.run(input_text)
            logger.info("Pipeline agen selesai tanpa error.")
            return input_text
        except Exception as e:
            logger.exception(f"Pipeline gagal: {str(e)}")
            raise
