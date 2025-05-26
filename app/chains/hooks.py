# app/chain/hooks.py

from typing import Callable, List, Any
from app.monitoring.logger import get_logger

logger = get_logger("ChainHooks", "hooks.log")

class Hooks:
    """
    Menyimpan dan menjalankan pre dan post hooks untuk chain.
    Hooks adalah fungsi callback yang dijalankan sebelum atau sesudah eksekusi utama chain.
    """

    def __init__(self):
        self.pre_hooks: List[Callable[[Any], Any]] = []
        self.post_hooks: List[Callable[[Any], Any]] = []

    def add_pre_hook(self, func: Callable[[Any], Any]):
        """Tambahkan fungsi hook yang dijalankan sebelum eksekusi utama chain."""
        self.pre_hooks.append(func)
        logger.info(f"Pre hook '{func.__name__}' ditambahkan.")

    def add_post_hook(self, func: Callable[[Any], Any]):
        """Tambahkan fungsi hook yang dijalankan setelah eksekusi utama chain."""
        self.post_hooks.append(func)
        logger.info(f"Post hook '{func.__name__}' ditambahkan.")

    def run_pre_hooks(self, data: Any) -> Any:
        """Jalankan semua pre hook secara berurutan dengan data sebagai input dan output."""
        logger.debug(f"Menjalankan {len(self.pre_hooks)} pre hooks.")
        for hook in self.pre_hooks:
            logger.debug(f"Menjalankan pre hook: {hook.__name__}")
            data = hook(data)
        return data

    def run_post_hooks(self, data: Any) -> Any:
        """Jalankan semua post hook secara berurutan dengan data sebagai input dan output."""
        logger.debug(f"Menjalankan {len(self.post_hooks)} post hooks.")
        for hook in self.post_hooks:
            logger.debug(f"Menjalankan post hook: {hook.__name__}")
            data = hook(data)
        return data
