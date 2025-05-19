# app/loaders/base_loader.py

from abc import ABC, abstractmethod
from typing import List

class BaseLoader(ABC):
    """
    Kelas dasar untuk semua loader. Semua loader harus mewarisi ini.
    """

    @abstractmethod
    def load(self, source: str) -> List[str]:
        """
        Memuat data dari sumber dan mengembalikan list teks.
        """
        pass
