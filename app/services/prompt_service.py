import os

class PromptService:
    def __init__(self):
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts')

    def get_prompt(self, agent_type):
        """Get the prompt template for a specific agent type."""
        valid_types = ['researcher', 'coder', 'planner']
        if agent_type not in valid_types:
            raise ValueError(f"Unsupported agent type: {agent_type}")

        prompt_file = os.path.join(self.prompts_dir, f'{agent_type}_prompts.txt')
        try:
            with open(prompt_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            raise ValueError(f"Prompt file not found for agent type: {agent_type}")

    def format_prompt(self, base_prompt, **kwargs):
        """Format a prompt template with the given parameters."""
        try:
            return base_prompt.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {e}") 