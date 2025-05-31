# app/memory/builder.py

from app.memory.registry import MEMORY_STORE_REGISTRY
from app.memory.base_memory import MemoryStore
from typing import Any

def build_memory_store(store_type: str, **kwargs) -> MemoryStore:
    """
    Factory method to build a memory store based on type.
    
    Args:
        store_type (str): Type of memory store, e.g., 'pgvector'.
        **kwargs: Parameters to pass to the store constructor.

    Returns:
        MemoryStore: An instance of a class implementing MemoryStore.
    """
    store_cls = MEMORY_STORE_REGISTRY.get(store_type.lower())
    if not store_cls:
        raise ValueError(f"Unknown memory store type: {store_type}")
    store_instance = store_cls(**kwargs)

    if not isinstance(store_instance, MemoryStore):
        raise TypeError(f"{store_cls.__name__} must inherit from MemoryStore")

    return store_instance
