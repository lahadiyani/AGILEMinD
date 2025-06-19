# app/tools/builder.py

from typing import Any
from app.tools.base_tool import BaseTool
from app.tools.registry_tool import get_tool

class ToolBuilder:
    """
    Builder/factory to create tool instances from the TOOL_REGISTRY.
    """

    @staticmethod
    def build(name: str, **config) -> BaseTool:
        """
        Build a tool instance based on the tool name and optional configuration.

        Args:
            name (str): Tool name as registered in TOOL_REGISTRY.
            **config: Dynamic configuration passed to the tool constructor.

        Returns:
            An instance of a class that inherits from BaseTool.

        Raises:
            KeyError: If the tool name is not found in the registry.
            Exception: If instantiation of the tool fails.
        """
        tool_cls = get_tool(name)
        instance = tool_cls(name=name, **config)
        return instance
