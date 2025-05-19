# app/loaders/utils.py

import os
from app.monitoring.logger import get_logger

logger = get_logger("LoaderUtils", "loader_utils.log", component="loaders")

def validate_path(path: str):
    if not os.path.exists(path):
        logger.error(f"Path tidak ditemukan: {path}")
        raise FileNotFoundError(f"Path tidak valid: {path}")
    return True
