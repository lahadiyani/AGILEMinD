from app.loaders.base_loader import BaseLoader
from app.monitoring.logger import get_logger
from app.loaders.custom.pdf_loader import PDFLoader
from app.loaders.custom.image_loader import ImageLoader  # Contoh loader lain

logger = get_logger("LoaderRegistry", "loader_registry.log", component="loaders")

LOADER_REGISTRY = {
    "PDFLoader": PDFLoader,
<<<<<<< HEAD
    "ImageLoader": ImageLoader
    # Anda bisa menambahkan loader lain di sini
    # "AnotherLoader": AnotherLoader,
=======
>>>>>>> fd8f606146b90d91279277340bc0ca95872ee949
}

def register_loader(name: str, cls: type, overwrite: bool = False):
    if not issubclass(cls, BaseLoader):
        logger.error(f"Gagal mendaftarkan loader {name}: bukan turunan BaseLoader")
        raise TypeError(f"{cls.__name__} harus turunan dari BaseLoader")
    
    if name in LOADER_REGISTRY and not overwrite:
        logger.warning(f"Loader '{name}' sudah terdaftar, tidak dilakukan overwrite tanpa izin.")
        raise ValueError(f"Loader '{name}' sudah ada di registry. Gunakan overwrite=True jika ingin mengganti.")
    
    LOADER_REGISTRY[name] = cls
    logger.info(f"Loader '{name}' berhasil didaftarkan.")

def get_loader(name: str):
    if name not in LOADER_REGISTRY:
        raise ValueError(f"Loader '{name}' tidak ditemukan di registry.")
    return LOADER_REGISTRY[name]

def list_loaders():
    return list(LOADER_REGISTRY.keys())
