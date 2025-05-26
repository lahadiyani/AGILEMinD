from app.loaders.registry import get_loader
from app.monitoring.logger import get_logger

logger = get_logger("LoaderBuilder", "builder.log", component="loaders")

def build_loader(config: dict):
    """
    Membuat loader berdasarkan konfigurasi.

    Args:
        config (dict): Konfigurasi loader, minimal harus ada:
            - "loader_name": str
            - "params": dict (optional)

    Returns:
        Instance dari loader yang sudah dibuat.

    Raises:
        ValueError: Jika 'loader_name' tidak ada atau loader tidak ditemukan.
        TypeError: Jika 'params' bukan dict.
        Exception: Jika konstruktor loader gagal.
    """
    loader_name = config.get("loader_name")
    if not loader_name:
        raise ValueError("Konfigurasi harus memiliki 'loader_name'.")

    params = config.get("params", {})
    if not isinstance(params, dict):
        raise TypeError(f"'params' harus berupa dict, tapi dapat {type(params)}")

    try:
        loader_class = get_loader(loader_name)
    except ValueError as e:
        logger.error(f"Loader '{loader_name}' tidak ditemukan: {e}")
        raise

    try:
        loader_instance = loader_class(**params)
    except Exception as e:
        logger.error(f"Gagal membuat instance loader '{loader_name}' dengan params {params}: {e}")
        raise

    logger.info(f"Loader '{loader_name}' berhasil dibuat dengan params {params}")
    return loader_instance
