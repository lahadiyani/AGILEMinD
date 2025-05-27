from flask import request, jsonify
from app.blueprints import agents_api
from app.controllers.agent_controller import AgentController

@agents_api.route('/run', methods=['POST'])
def run_agent():
    """
    Endpoint universal untuk menjalankan agent dari registry.
    Expects JSON: { "agent_type": "...", "prompt": "..." }
    """
    agent_controller = AgentController()
    return agent_controller.agent_endpoint()