from app.services.orchestrator import AgentOrchestrator
from flask import request, jsonify, current_app, render_template

class AgentController:
    def __init__(self, agent_name=None):
        self.agent_name = agent_name

    def run_agent(self, agent_type, prompt, model=None):
        """
        Menjalankan agent dari orchestrator berdasarkan agent_type dan prompt.
        """
        orchestrator = AgentOrchestrator()
        # Kirim parameter model jika ada
        result = orchestrator.run(agent_type, prompt, model=model)
        return result

    # Contoh endpoint Flask
    def agent_endpoint(self):
        """
        Endpoint universal untuk menjalankan agent.
        Expects JSON: { "agent_type": "...", "prompt": "...", "model": "..." }
        """
        data = request.get_json()
        agent_type = data.get("agent_type")
        prompt = data.get("prompt")
        model = data.get("model")  # ambil model jika ada

        if not agent_type or not prompt:
            return jsonify({"status": "error", "message": "agent_type and prompt are required"}), 400

        result = self.run_agent(agent_type, prompt, model=model)
        return jsonify(result)
