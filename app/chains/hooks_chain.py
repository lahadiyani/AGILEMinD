from typing import Callable, List, Any

class Hooks:
    """
    Menyimpan dan menjalankan pre dan post hooks untuk chain.
    Hooks adalah fungsi callback yang dijalankan sebelum atau sesudah eksekusi utama chain.
    """

    def __init__(self, verbose: bool = True):
        self.pre_hooks: List[Callable[[Any], Any]] = []
        self.post_hooks: List[Callable[[Any], Any]] = []
        self.verbose = verbose

    def add_pre_hook(self, func: Callable[[Any], Any]) -> None:
        """Tambahkan fungsi hook yang dijalankan sebelum eksekusi utama chain."""
        self.pre_hooks.append(func)
        if self.verbose:
            print(f"[ChainHooks] Pre hook '{getattr(func, '__name__', repr(func))}' ditambahkan.")

    def add_post_hook(self, func: Callable[[Any], Any]) -> None:
        """Tambahkan fungsi hook yang dijalankan setelah eksekusi utama chain."""
        self.post_hooks.append(func)
        if self.verbose:
            print(f"[ChainHooks] Post hook '{getattr(func, '__name__', repr(func))}' ditambahkan.")

    def run_pre_hooks(self, data: Any) -> Any:
        """Jalankan semua pre hook secara berurutan dengan data sebagai input dan output."""
        if self.verbose:
            print(f"[ChainHooks] Menjalankan {len(self.pre_hooks)} pre hooks.")
        for hook in self.pre_hooks:
            if self.verbose:
                print(f"[ChainHooks] Menjalankan pre hook: {getattr(hook, '__name__', repr(hook))}")
            data = hook(data)
        return data

    def run_post_hooks(self, data: Any) -> Any:
        """Jalankan semua post hook secara berurutan dengan data sebagai input dan output."""
        if self.verbose:
            print(f"[ChainHooks] Menjalankan {len(self.post_hooks)} post hooks.")
        for hook in self.post_hooks:
            if self.verbose:
                print(f"[ChainHooks] Menjalankan post hook: {getattr(hook, '__name__', repr(hook))}")
            data = hook(data)
        return data
