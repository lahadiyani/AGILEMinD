# app/loaders/registry.py

from app.loaders.base_loader import BaseLoader
from app.monitoring.logger import get_logger
from app.loaders.custom.pdf_loader import PDFLoader

logger = get_logger("LoaderRegistry", "loader_registry.log", component="loaders")

# Registry untuk semua loader yang terdaftar
LOADER_REGISTRY = {
    "PDFLoader": PDFLoader,
    # Anda bisa menambahkan loader lain di sini
    # "AnotherLoader": AnotherLoader,
}

def register_loader(name: str, cls: type):
    if not issubclass(cls, BaseLoader):
        logger.error(f"Gagal mendaftarkan loader {name}: bukan turunan BaseLoader")
        raise TypeError(f"{cls.__name__} harus turunan dari BaseLoader")
    
    LOADER_REGISTRY[name] = cls
    logger.info(f"Loader '{name}' berhasil didaftarkan.")

def get_loader(name: str):
    if name not in LOADER_REGISTRY:
        raise ValueError(f"Loader '{name}' tidak ditemukan di registry.")
    return LOADER_REGISTRY[name]
