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
    
    def pollinations_text(self, prompt, model=None):
        try:
            response = generate_text(prompt, model)
            if isinstance(response, str) and response.startswith("Error:"):
                return {"status": "error", "error": response}
            return {"status": "success", "response": response}
        except Exception as e:
            current_app.logger.error(f"Error generating text: {e}")
            return {"status": "error", "error": str(e)}
    
    def pollinations_image(self, prompt, model=None):
        try:
            # Generate image using Pollinations API
            image_data = generate_image(prompt, model)
            
            if isinstance(image_data, str) and image_data.startswith("Error:"):
                return {"status": "error", "error": image_data}

            # Ensure the output directory exists
            output_dir = os.path.join(current_app.static_folder, 'output', 'images')
            os.makedirs(output_dir, exist_ok=True)

            # Save the image
            image_path = os.path.join(output_dir, 'generated_image.jpg')
            with open(image_path, 'wb') as f:
                f.write(image_data)

            # Return the relative path for the frontend
            return {
                "status": "success",
                "image_path": "/static/output/images/generated_image.jpg"
            }

        except Exception as e:
            current_app.logger.error(f"Error generating image: {e}")
            return {"status": "error", "error": str(e)}

    def process_agent_request(self, agent_type, prompt, model=None):
        try:
            if agent_type not in ['researcher', 'coder', 'planner']:
                return {"status": "error", "error": "Unsupported agent type"}

            # Get the base prompt template
            base_prompt = self.prompt_service.get_prompt(agent_type)
            
            # Format the prompt with user input
            formatted_prompt = f"{base_prompt}\n\nUser Input: {prompt}"
            
            # Generate response using Pollinations API
            response = generate_text(formatted_prompt, model)
            
            if isinstance(response, str) and response.startswith("Error:"):
                return {"status": "error", "error": response}

            return {
                "status": "success",
                "response": response,
                "agent_type": agent_type
            }

        except Exception as e:
            current_app.logger.error(f"Error processing {agent_type} request: {e}")
            return {"status": "error", "error": str(e)}