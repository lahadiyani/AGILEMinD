import logging
import os

# Root folder logging
BASE_LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')

def ensure_log_dir(component: str) -> str:
    """
    Membuat folder log untuk komponen tertentu jika belum ada.
    :param component: Nama subfolder (misal: 'agents', 'chains', dll)
    :return: Path folder log
    """
    log_dir = os.path.join(BASE_LOG_DIR, component)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir

def get_logger(name: str, filename: str, component: str = 'default') -> logging.Logger:
    """
    Mendapatkan logger untuk komponen/folder apapun.
    :param name: Nama logger
    :param filename: Nama file log (misal: agent1.log)
    :param component: Nama subfolder log (misal: 'agents', 'chains', 'tasks', dll)
    :return: objek Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_dir = ensure_log_dir(component)
    log_path = os.path.join(log_dir, filename)
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Cek jika handler sudah ada supaya tidak duplikat
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

# Contoh penggunaan:
# agent_logger = get_logger('my_agent', 'agent1.log', component='agents')
# chain_logger = get_logger('my_chain', 'chain1.log', component='chains')
# task_logger = get_logger('my_task', 'task1.log', component='tasks')