import logging
import os

# Folder untuk log per komponen agen
agents_log_root_dir = os.path.join(os.path.dirname(__file__), 'agents')
os.makedirs(agents_log_root_dir, exist_ok=True)

def get_agent_logger(name: str, filename: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_path = os.path.join(agents_log_root_dir, filename)
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(formatter)

    # Tambah console output juga (opsional)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
