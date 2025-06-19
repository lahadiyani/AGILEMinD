# app/tools/utils.py

import inspect
from typing import Type
from app.tools.base_tool import BaseTool

def is_tool_class(obj: object) -> bool:
    """
    Check if the object is a class that inherits from BaseTool.

    Args:
        obj (object): The object to check.

    Returns:
        bool: True if obj is a subclass of BaseTool, False otherwise.
    """
    return inspect.isclass(obj) and issubclass(obj, BaseTool)

def get_tool_name(tool_cls: Type[BaseTool]) -> str:
    """
    Get the name of a tool class.

    Args:
        tool_cls (Type[BaseTool]): The tool class.

    Returns:
        str: Name of the tool, defaulting to class name if 'name' attribute is not defined.
    """
    return getattr(tool_cls, "name", tool_cls.__name__)

def safe_execute(tool_instance: BaseTool, *args, **kwargs):
    """
    Safely execute the 'execute' method of a tool instance.

    Args:
        tool_instance (BaseTool): The tool instance.
        *args: Positional arguments for the execute method.
        **kwargs: Keyword arguments for the execute method.

    Returns:
        The result of the execute method.

    Raises:
        Exception: Any exception raised by the execute method.
    """
    try:
        return tool_instance.execute(*args, **kwargs)
    except Exception as e:
        raise e  # Custom handling can be added here if needed

def list_registered_tools(registry: dict) -> list[str]:
    """
    List all registered tool names in a given registry.

    Args:
        registry (dict): The tool registry dictionary.

    Returns:
        list[str]: List of registered tool names.
    """
    return list(registry.keys())
