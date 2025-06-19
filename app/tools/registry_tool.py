# app/tools/registry.py

from app.tools.base_tool import BaseTool
from app.tools.custom.custom_tool import CustomTool
from app.tools.custom.image_downloader import ImageDownloaderTool

# Manual registry of tools
TOOL_REGISTRY = {
    "CustomTool": CustomTool,
    "ImageDownloaderTool": ImageDownloaderTool,
    # Add more tools here as needed
}

def validate_tool_registry(registry: dict):
    """
    Validate that all entries in the registry are subclasses of BaseTool.
    """
    for name, cls in registry.items():
        if not isinstance(cls, type):
            raise TypeError(f"Tool '{name}' must be a class (type), got {type(cls)} instead.")
        if not issubclass(cls, BaseTool):
            raise TypeError(f"Tool '{name}' must subclass BaseTool, but got {cls}.")

def get_tool(name: str) -> type[BaseTool]:
    """
    Retrieve a tool class by name from the registry.

    Args:
        name (str): Tool name.

    Returns:
        type[BaseTool]: The tool class.

    Raises:
        KeyError: If the tool name is not found in the registry.
    """
    tool_cls = TOOL_REGISTRY.get(name)
    if tool_cls is None:
        raise KeyError(f"Tool '{name}' not found in TOOL_REGISTRY")
    return tool_cls

def list_tools() -> list[str]:
    """
    Return a list of all registered tool names.

    Returns:
        list[str]: Registered tool names.
    """
    return list(TOOL_REGISTRY.keys())
