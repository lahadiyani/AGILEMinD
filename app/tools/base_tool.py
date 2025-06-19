# app/tools/base_tools.py

from abc import ABC, abstractmethod

class BaseTool(ABC):
    """
    Abstract base class for all tools.
    Tools extending BaseTool must implement the execute() method.
    """

    def __init__(self, name: str = None, host: str = None, **kwargs):
        """
        Initialize the tool with an optional name and config.
        """
        self.name = name or self.__class__.__name__
        self.config = kwargs
        self.host = host

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Main method to run the tool.
        Must be overridden in the subclass.
        """
        pass

    def run(self, *args, **kwargs):
        """
        Wrapper method to run the tool.
        Can be extended to handle exceptions or post-processing.
        """
        return self.execute(*args, **kwargs)

    def update_config(self, **kwargs):
        """
        Dynamically update the tool's configuration.
        """
        self.config.update(kwargs)

    def clear(self):
        """
        Optional method for cleanup.
        """
        pass

    def load(self):
        """
        Optional method for loading necessary data or state.
        """
        pass
