# app/tools/builder.py

from typing import Any, Dict, Optional
from app.tools.base_tool import BaseTool
from app.tools.registry import get_tool

class ToolBuilder:
    """
    Builder/factory untuk membuat instance tool dari TOOL_REGISTRY.
    """

    @staticmethod
    def build(name: str, **config) -> BaseTool:
        """
        Membangun instance tool berdasarkan nama tool dan konfigurasi opsional.

        Args:
            name (str): Nama tool yang terdaftar di TOOL_REGISTRY.
            **config: konfigurasi dinamis yang diteruskan ke konstruktor tool.

        Returns:
            instance BaseTool turunan.
        
        Raises:
            KeyError jika nama tool tidak ditemukan.
            Exception dari konstruktor tool jika gagal.
        """
        tool_cls = get_tool(name)
        instance = tool_cls(name=name, **config)
        return instance
