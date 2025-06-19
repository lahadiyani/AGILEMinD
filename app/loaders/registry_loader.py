from app.loaders.base_loader import BaseLoader
from app.loaders.custom.pdf_loader import PDFLoader
from app.loaders.custom.image_loader import ImageLoader  # Example of another loader

LOADER_REGISTRY = {
    "PDFLoader": PDFLoader,
    "ImageLoader": ImageLoader
    # You can add other loaders here
    # "AnotherLoader": AnotherLoader,
}

def register_loader(name: str, cls: type, overwrite: bool = False):
    """
    Register a loader class to the loader registry.

    Args:
        name (str): The unique name for the loader.
        cls (type): The class of the loader, must subclass BaseLoader.
        overwrite (bool): Whether to overwrite an existing loader with the same name.

    Raises:
        TypeError: If cls is not a subclass of BaseLoader.
        ValueError: If loader is already registered and overwrite is False.
    """
    if not issubclass(cls, BaseLoader):
        raise TypeError(f"{cls.__name__} must be a subclass of BaseLoader")

    if name in LOADER_REGISTRY and not overwrite:
        raise ValueError(f"Loader '{name}' already exists in the registry. Use overwrite=True to replace it.")

    LOADER_REGISTRY[name] = cls

def get_loader(name: str):
    """
    Retrieve a loader class by name.

    Args:
        name (str): The name of the loader.

    Returns:
        type: The loader class.

    Raises:
        ValueError: If the loader is not found in the registry.
    """
    if name not in LOADER_REGISTRY:
        raise ValueError(f"Loader '{name}' not found in the registry.")
    return LOADER_REGISTRY[name]

def list_loaders():
    """
    List all registered loader names.

    Returns:
        list: List of loader names.
    """
    return list(LOADER_REGISTRY.keys())
