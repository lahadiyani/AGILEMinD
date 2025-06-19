from app.agents.builder_agent import build_agent

class AgentOrchestrator:
    def __init__(self, agent_name=None):
        self.agent_name = agent_name

    def run(self, agent_type, prompt, model=None):
        """
        Menjalankan agent sesuai agent_type, prompt, dan model (opsional).
        """
        config = {
            "agent_name": agent_type,
            "params": {
                "name": agent_type,
                "description": f"{agent_type} agent",
                "prompt": "{input}",
                "llm_name": model if model else None  # Jika model diberikan, gunakan sebagai llm_name
            }
        }
        # Hapus llm_name jika None agar tidak mengganggu agent yang tidak butuh llm_name
        if not config["params"]["llm_name"]:
            config["params"].pop("llm_name")

        try:
            agent = build_agent(config)
            import inspect
            sig = inspect.signature(agent.run)
            # Cek apakah run menerima parameter model
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
