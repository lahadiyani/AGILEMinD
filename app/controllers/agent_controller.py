from app.services.agent_orchestrator import AgentOrchestrator
from app.tools.pollination import generate_text, generate_image
from app.services.prompt_service import PromptService
from flask import request, jsonify, current_app
import os


class AgentController:
    def __init__(self, agent_name=None):
        self.agent_name = agent_name
        self.prompt_service = PromptService()

    def get_agent_data(self):
        orchestrator = AgentOrchestrator(self.agent_name)
        return orchestrator.run()

    def list_agents(self):
        orchestrator = AgentOrchestrator()
        return orchestrator.list_all_agents()
    
    def pollinations_text(self, prompt):
        result = generate_text(prompt)
        return jsonify({"text": result})
    
    def pollinations_image(self, prompt):
        try:
            # Generate the image from the prompt
            image_data = generate_image(prompt)
            
            # Check if the response is an error message
            if isinstance(image_data, str) and image_data.startswith("Error:"):
                return jsonify({"error": image_data}), 500

            # Get the absolute path to the static directory
            static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'app', 'static')
            assets_dir = os.path.join(static_dir, 'assets')

            # Ensure the 'assets' directory exists
            if not os.path.exists(assets_dir):
                os.makedirs(assets_dir)

            # Define the image path where the file will be saved
            image_filename = "generated_image.jpg"
            image_path = os.path.join(assets_dir, image_filename)

            # Save the image data to the file
            with open(image_path, "wb") as f:
                f.write(image_data)

            # Log the image saving process
            current_app.logger.info(f"Image saved at {image_path}")

            # Return the correct path to the image (relative to static directory)
            return jsonify({"image_path": f"/static/assets/{image_filename}"})

        except Exception as e:
            current_app.logger.error(f"Error generating image: {e}")
            return jsonify({"error": str(e)}), 500

    def process_agent_request(self, agent_type, prompt):
        """Process request for different agent types"""
        try:
            # Format the prompt with the appropriate template
            formatted_prompt = self.prompt_service.format_prompt(agent_type, prompt)
            
            # Generate response using Pollinations text API
            response = generate_text(formatted_prompt)
            
            if isinstance(response, str) and response.startswith("Error:"):
                return jsonify({"error": response}), 500
                
            return jsonify({
                "agent_type": agent_type,
                "prompt": prompt,
                "response": response
            })
            
        except Exception as e:
            current_app.logger.error(f"Error processing {agent_type} request: {e}")
            return jsonify({"error": str(e)}), 500