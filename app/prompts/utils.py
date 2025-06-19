import os

class PromptUtils:
    PROMPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "prompts", "prompt"))
    _cache = {}

    @classmethod
    def load_prompt(cls, filename: str) -> str:
        """
        Load prompt text from file in PROMPT_DIR.

        Args:
            filename (str): Name of the prompt file.

        Returns:
            str: Prompt content.

        Raises:
            FileNotFoundError: If the file is not found.
            IOError: If the file fails to read.
        """
        if filename in cls._cache:
            return cls._cache[filename]

        path = os.path.join(cls.PROMPT_DIR, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt file not found: {path}")

        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                cls._cache[filename] = content
                return content
        except Exception as e:
            raise IOError(f"Failed to read prompt file {path}: {e}")
