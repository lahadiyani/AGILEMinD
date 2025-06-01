# app/tools/registry.py
from app.tools.base_tool import BaseTool
from app.tools.custom.custom_tool import CustomTool
from app.tools.custom.image_downloader import ImageDownloaderTool

# Registrasi tool secara manual di dictionary ini
TOOL_REGISTRY = {
    "CustomTool": CustomTool,
    "ImageDownloaderTool": ImageDownloaderTool,
    # Tambahkan tool lain di sini jika ada
}

def validate_tool_registry(registry: dict):
    """
    Validasi bahwa semua kelas di registry adalah subclass dari BaseTool.
    """
    for name, cls in registry.items():
        if not isinstance(cls, type):
            raise TypeError(f"Tool '{name}' harus berupa kelas (type), tapi dapat {type(cls)}")
        if not issubclass(cls, BaseTool):
            raise TypeError(f"Tool '{name}' harus subclass dari BaseTool, tapi {cls} bukan.")

# Jalankan validasi saat import modul
validate_tool_registry(TOOL_REGISTRY)

def get_tool(name: str) -> BaseTool:
    """
    Ambil kelas tool berdasarkan nama dari registry.
    Raise KeyError jika tool tidak ditemukan.
    """
    tool_cls = TOOL_REGISTRY[name] if name in TOOL_REGISTRY else None
    tool_cls = TOOL_REGISTRY.get(name)
    if tool_cls is None:
        raise KeyError(f"Tool '{name}' tidak ditemukan di TOOL_REGISTRY")
    return tool_cls

def list_tools() -> list[str]:
    """
    Kembalikan list nama tool yang terdaftar di registry.
    """
    return list(TOOL_REGISTRY.keys())
