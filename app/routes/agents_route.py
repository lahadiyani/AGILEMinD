from flask import request, jsonify, current_app
import logging
from app.blueprints import agents_api
from app.controllers.agent_controller import AgentController
from app.services.agent_orchestrator import AgentOrchestrator
from app.tools.pollination import get_available_image_models, get_available_text_models

logging.basicConfig(level=logging.INFO)

@agents_api.route('/models/image', methods=['GET'])
def get_image_models():
    try:
        # Get image models using the pollination tool
        models = get_available_image_models()
        
        if isinstance(models, str) and models.startswith("Error:"):
            return jsonify({
                "status": "error",
                "message": models
            }), 500
            
        return jsonify({
            "status": "success",
            "models": models
        })
    except Exception as e:
        logging.error(f"Error fetching image models: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@agents_api.route('/models/text', methods=['GET'])
def get_text_models():
    try:
        # Get text models using the pollination tool
        models = get_available_text_models()
        
        if isinstance(models, str) and models.startswith("Error:"):
            return jsonify({
                "status": "error",
                "message": models
            }), 500
            
        return jsonify({
            "status": "success",
            "models": models
        })
    except Exception as e:
        logging.error(f"Error fetching text models: {e}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@agents_api.route('/<string:agent_name>', methods=['POST'])
def get_agent(agent_name):
    try:
        # Extract data from the request body
        data = request.get_json()
        prompt = data.get('prompt')
        agent_type = data.get('agent_type')
        model = data.get('model')  # Get optional model parameter

        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # Initialize the controller
        agent_controller = AgentController(agent_name)

        # Process based on agent type
        if agent_type in ['researcher', 'coder', 'planner']:
            return agent_controller.process_agent_request(agent_type, prompt, model)
        elif agent_type == 'pollinations':
            # Handle Pollinations specific requests
            if prompt.startswith("buatkan saya gambar"):
                return agent_controller.pollinations_image(prompt, model)
            else:
                return agent_controller.pollinations_text(prompt, model)
        else:
            return jsonify({"error": "Unsupported agent type"}), 400

    except Exception as e:
        logging.error(f"Error in get_agent: {e}")
        return jsonify({"error": str(e)}), 500

@agents_api.route('/list', methods=['GET'])
def list_agents():
    agent_controller = AgentController()
    agent_list = agent_controller.list_agents()
    return jsonify(agent_list)

@agents_api.route('/pollinations/text', methods=['POST'])
def pollinations_text():
    try:
        data = request.json
        prompt = data.get('prompt')
        model = data.get('model')  # Get optional model parameter
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
            
        agent_controller = AgentController()
        result = agent_controller.pollinations_text(prompt, model)
        return result
    except Exception as e:
        logging.error(f"Error in pollinations_text: {e}")
        return jsonify({"error": str(e)}), 500

@agents_api.route('/pollinations/image', methods=['POST'])
def pollinations_image():
    try:
        data = request.json
        prompt = data.get('prompt')
        model = data.get('model')  # Get optional model parameter
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
            
        agent_controller = AgentController()
        result = agent_controller.pollinations_image(prompt, model)
        return result
    except Exception as e:
        logging.error(f"Error in pollinations_image: {e}")
        return jsonify({"error": str(e)}), 500
