# app/loaders/builder.py

from app.loaders.registry import get_loader
from app.monitoring.logger import get_logger

logger = get_logger("LoaderBuilder", "builder.log", component="loaders")

def build_loader(config: dict):
    """
    Membuat loader berdasarkan konfigurasi.
    
    config: {
        "loader_name": str,
        "params": dict (optional)
    }
    """
    loader_name = config.get("loader_name")
    if not loader_name:
        raise ValueError("Konfigurasi harus memiliki 'loader_name'.")

    loader_class = get_loader(loader_name)
    params = config.get("params", {})

    logger.info(f"Membangun loader '{loader_name}' dengan params {params}")
    return loader_class(**params)
