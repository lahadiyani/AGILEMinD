import logging
import os

# Root folder logging untuk agents dan chains
BASE_LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
AGENTS_LOG_DIR = os.path.join(BASE_LOG_DIR, 'agents')
CHAINS_LOG_DIR = os.path.join(BASE_LOG_DIR, 'chains')

# Buat folder jika belum ada
os.makedirs(AGENTS_LOG_DIR, exist_ok=True)
os.makedirs(CHAINS_LOG_DIR, exist_ok=True)

def get_logger(name: str, filename: str, component: str = 'agents') -> logging.Logger:
    """
    Mendapatkan logger untuk komponen tertentu (agents/chains).
    :param name: Nama logger
    :param filename: Nama file log (misal: agent1.log)
    :param component: 'agents' atau 'chains'
    :return: objek Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if component == 'chains':
        log_dir = CHAINS_LOG_DIR
    else:
        log_dir = AGENTS_LOG_DIR

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
