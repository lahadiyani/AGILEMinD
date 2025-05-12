import os

class PromptService:
    def __init__(self):
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts')
        
    def get_prompt(self, agent_type):
        """Get the prompt template for a specific agent type"""
        prompt_file = os.path.join(self.prompts_dir, f'{agent_type}_prompts.txt')
        try:
            with open(prompt_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return f"Error: Prompt template for {agent_type} not found"
            
    def format_prompt(self, agent_type, user_input):
        """Format the prompt with user input"""
        base_prompt = self.get_prompt(agent_type)
        return f"{base_prompt}\n\nUser Input: {user_input}" 