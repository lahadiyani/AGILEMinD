import os
from app.monitoring.logger import get_logger

class PromptUtils:
    logger = get_logger("PromptUtils", "prompts_utils.log", component="prompts")
    PROMPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "prompts"))
    _cache = {}

    @classmethod
    def load_prompt(cls, filename: str) -> str:
        """
        Load prompt text from file in PROMPT_DIR.

        Args:
            filename (str): Nama file prompt.

        Returns:
            str: Konten prompt.

        Raises:
            FileNotFoundError: Jika file tidak ditemukan.
            IOError: Jika gagal membaca file.
        """
        if filename in cls._cache:
            return cls._cache[filename]

        path = os.path.join(cls.PROMPT_DIR, filename)
        if not os.path.exists(path):
            cls.logger.error(f"Prompt file tidak ditemukan: {path}")
            raise FileNotFoundError(f"Prompt file not found: {path}")

        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                cls._cache[filename] = content
                return content
        except Exception as e:
            cls.logger.error(f"Gagal baca prompt file {path}: {e}")
            raise
