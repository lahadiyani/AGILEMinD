from app.agents.registry import AGENT_REGISTRY

class AgentOrchestrator:
    """
    Orchestrator untuk mengambil dan menjalankan agent berdasarkan nama/type agent.
    """

    def __init__(self, agent_name=None):
        self.agent_name = agent_name

    def get_agent_class(self, agent_type):
        """
        Mengambil agent class dari registry berdasarkan nama/type.
        """
        return AGENT_REGISTRY.get(agent_type)

    def create_agent_instance(self, agent_class, agent_type):
        """
        Membuat instance agent dengan parameter yang sesuai konstruktor agent.
        """
        # Cek signature konstruktor agent
        import inspect
        params = inspect.signature(agent_class.__init__).parameters
        kwargs = {}

        # Lewati 'self'
        param_names = list(params.keys())[1:]

        # Siapkan nilai default
        default_values = {
            "name": agent_type,
            "description": getattr(agent_class, "__doc__", "") or f"{agent_type} agent",
            "prompt": "{input}"
        }

        for pname in param_names:
            if pname in default_values:
                kwargs[pname] = default_values[pname]

        return agent_class(**kwargs)

    def run(self, agent_type, prompt, model=None):
        """
        Menjalankan agent berdasarkan tipe dan prompt yang diberikan.
        """
        agent_class = self.get_agent_class(agent_type)
        if not agent_class:
            return {"status": "error", "message": "Unsupported agent type"}

        agent = self.create_agent_instance(agent_class, agent_type)
        try:
            # Jika agent.run mendukung parameter model, gunakan
            import inspect
            sig = inspect.signature(agent.run)
            if "model" in sig.parameters:
                result = agent.run(prompt, model=model)
            else:
                result = agent.run(prompt)
            return {
                "status": "success",
                "result": result,
                "agent_name": getattr(agent, "name", agent_type),
                "agent_description": getattr(agent, "description", "")
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}