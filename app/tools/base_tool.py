# app/tools/base_tools.py

from abc import ABC, abstractmethod
from app.monitoring.logger import get_logger

class BaseTool(ABC):
    """
    Abstract base class untuk semua tool.
    Tool yang di-extend dari BaseTool harus mengimplementasikan method execute().
    """

    def __init__(self, name: str = None, host: str = None, **kwargs):
        """
        Inisialisasi tool dengan nama dan konfigurasi opsional.
        """
        self.name = name or self.__class__.__name__
        self.config = kwargs
        self.host = host
        self.logger = get_logger(self.name, f"{self.name.lower()}.log")
        self.logger.info(f"Tool '{self.name}' initialized with config: {self.config}")

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Method utama untuk menjalankan tool.
        Harus dioverride di subclass.
        """
        pass

    def run(self, *args, **kwargs):
        """
        Wrapper untuk menjalankan tool dengan logging dan error handling.
        """
        self.logger.info(f"Running tool '{self.name}' with args={args}, kwargs={kwargs}")
        try:
            result = self.execute(*args, **kwargs)
            self.logger.info(f"Tool '{self.name}' executed successfully.")
            return result
        except Exception as e:
            self.logger.error(f"Error executing tool '{self.name}': {e}", exc_info=True)
            raise

    def update_config(self, **kwargs):
        """
        Update konfigurasi tool secara dinamis.
        """
        self.config.update(kwargs)
        self.logger.info(f"Tool '{self.name}' config updated: {kwargs}")

    def clear(self):
        pass

    def load(self):
        pass
