# app/tools/utils.py

import inspect
from typing import Type
from app.tools.base_tools import BaseTool

def is_tool_class(obj: object) -> bool:
    """
    Cek apakah objek merupakan kelas turunan BaseTool.
    
    Args:
        obj: objek yang akan dicek.
    
    Returns:
        bool: True jika obj adalah subclass BaseTool, False jika bukan.
    """
    return inspect.isclass(obj) and issubclass(obj, BaseTool)

def get_tool_name(tool_cls: Type[BaseTool]) -> str:
    """
    Ambil nama tool dari kelas tool.
    
    Args:
        tool_cls: kelas tool.
        
    Returns:
        str: nama tool (default: nama kelas).
    """
    return getattr(tool_cls, "name", tool_cls.__name__)

def safe_execute(tool_instance: BaseTool, *args, **kwargs):
    """
    Jalankan method `execute` tool dengan penanganan error terstruktur.
    
    Args:
        tool_instance: instance dari tool.
        *args, **kwargs: argumen untuk method execute.
    
    Returns:
        hasil dari execute jika sukses.
    
    Raises:
        Exception jika terjadi error saat execute (error sudah dicatat oleh tool).
    """
    try:
        return tool_instance.execute(*args, **kwargs)
    except Exception as e:
        # Biasanya logging sudah dilakukan di BaseTool.run
        # Tapi untuk utility ini bisa buat penanganan khusus jika perlu
        raise e

def list_registered_tools(registry: dict) -> list[str]:
    """
    Ambil daftar nama tool yang terdaftar pada registry tertentu.
    
    Args:
        registry (dict): dictionary registry tool.
        
    Returns:
        list[str]: daftar nama tool yang terdaftar.
    """
    return list(registry.keys())
