import os
from app.monitoring.logger import get_logger

logger = get_logger("LoaderUtils", "loader_utils.log", component="loaders")

def validate_path(path: str, must_be_file: bool = False, must_be_dir: bool = False):
    """
    Validasi keberadaan path dan tipe path.

    Args:
        path (str): Path yang ingin divalidasi.
        must_be_file (bool): Jika True, path harus file.
        must_be_dir (bool): Jika True, path harus direktori.

    Raises:
        FileNotFoundError: Jika path tidak ada.
        ValueError: Jika tipe path tidak sesuai.
        PermissionError: Jika path tidak dapat dibaca.
    """
    if not os.path.exists(path):
        logger.error(f"Path tidak ditemukan: {path}")
        raise FileNotFoundError(f"Path tidak ditemukan: {path}")

    if must_be_file and not os.path.isfile(path):
        logger.error(f"Path bukan file: {path}")
        raise ValueError(f"Path bukan file: {path}")

    if must_be_dir and not os.path.isdir(path):
        logger.error(f"Path bukan direktori: {path}")
        raise ValueError(f"Path bukan direktori: {path}")

    if not os.access(path, os.R_OK):
        logger.error(f"Tidak punya akses baca ke path: {path}")
        raise PermissionError(f"Tidak punya akses baca ke path: {path}")
