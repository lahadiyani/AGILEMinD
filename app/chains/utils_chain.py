import time
from typing import Callable, Any

def timeit(func: Callable) -> Callable:
    """
    Decorator to measure the execution time of a function.
    Useful for monitoring chain or agent performance.
    """
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[timeit] Function '{func.__name__}' executed in {elapsed:.4f} seconds.")
        return result
    return wrapper

def safe_run(func: Callable, *args, **kwargs) -> Any:
    """
    Execute a function with try-except to prevent crashes.
    Useful for robust execution in chains or agents.
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"[safe_run] Error during '{func.__name__}': {str(e)}")
        raise

def chunk_text(text: str, max_length: int) -> list[str]:
    """
    Split long text into chunks with a maximum length.
    Useful for document chunking before embedding or retrieval.
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
    Flatten a nested list into a single flat list.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
