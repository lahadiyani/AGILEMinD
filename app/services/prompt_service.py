import os
from app.prompts.utils import PromptUtils

class PromptService:
    def __init__(self):
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts')

    def get_prompt(self, agent_type):
        """Get the prompt template for a specific agent type."""
        valid_types = ['researcher', 'coder', 'planner']
        if agent_type not in valid_types:
            raise ValueError(f"Unsupported agent type: {agent_type}")

        prompt_filename = f'{agent_type}_prompts.txt'
        try:
            # Gunakan PromptUtils.load_prompt agar caching dan logging aktif
            return PromptUtils.load_prompt(prompt_filename).strip()
        except FileNotFoundError:
            raise ValueError(f"Prompt file not found for agent type: {agent_type}")

    def format_prompt(self, base_prompt, **kwargs):
        """Format a prompt template with the given parameters."""
        try:
            return base_prompt.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {e}")
