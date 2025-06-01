from app.agents.builder import build_agent

class AgentOrchestrator:
    def __init__(self, agent_name=None):
        self.agent_name = agent_name

    def run(self, agent_type, prompt, model=None):
        config = {
            "agent_name": agent_type,
            "params": {
                "name": agent_type,
                "description": f"{agent_type} agent",
                "prompt": "{input}"
            }
        }

        try:
            agent = build_agent(config)
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
