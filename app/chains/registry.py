# app/chain/registry.py

from app.chains.base_chain import BaseChain
from app.chains.custom.custom_chain import CustomChain  # Contoh chain custom yang kamu buat

from app.monitoring.logger import get_logger

logger = get_logger("ChainRegistry", "registry.log")

# Registry untuk semua chain yang tersedia di framework
CHAIN_REGISTRY = {
    "BaseChain": BaseChain,
    "CustomChain": CustomChain,
    # Tambahkan chain lain di sini
}

def register_chain(chain_name: str, chain_class: type):
    """
    Daftarkan chain baru ke registry.
    
    Args:
        chain_name (str): Nama unik untuk chain
        chain_class (type): Kelas chain yang merupakan subclass dari BaseChain
    
    Raises:
        TypeError: Jika chain_class bukan subclass BaseChain
    """
    if not issubclass(chain_class, BaseChain):
        logger.error(f"Gagal mendaftarkan chain: {chain_class.__name__} bukan turunan BaseChain.")
        raise TypeError(f"{chain_class.__name__} is not a subclass of BaseChain.")
    
    CHAIN_REGISTRY[chain_name] = chain_class
    logger.info(f"Chain '{chain_name}' berhasil didaftarkan.")
