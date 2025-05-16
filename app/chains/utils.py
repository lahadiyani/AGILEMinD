# app/chain/utils.py

import time
from typing import Callable, Any
from app.monitoring.logger import get_agent_logger

logger = get_agent_logger("ChainUtils", "utils.log")

def timeit(func: Callable) -> Callable:
    """
    Decorator untuk mengukur waktu eksekusi fungsi.
    Berguna untuk monitoring performa chain atau agent.
    """
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"Function '{func.__name__}' executed in {elapsed:.4f} seconds.")
        return result
    return wrapper

def safe_run(func: Callable, *args, **kwargs) -> Any:
    """
    Menjalankan fungsi dengan try-except untuk menghindari crash dan log error.
    Cocok untuk eksekusi chain atau agent yang harus tahan terhadap error.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Error during '{func.__name__}': {str(e)}")
        raise

def chunk_text(text: str, max_length: int) -> list[str]:
    """
    Membagi teks panjang menjadi beberapa bagian sesuai max_length.
    Berguna untuk chunking dokumen sebelum embedding atau retrieval.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_length
        chunks.append(text[start:end])
        start = end
    return chunks

def flatten_list(nested_list: list) -> list:
    """
    Meratakan list bersarang menjadi list satu dimensi.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
