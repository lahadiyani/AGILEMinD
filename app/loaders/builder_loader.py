from app.loaders.registry_loader import get_loader

def build_loader(config: dict):
    """
    Build a loader instance based on configuration.

    Args:
        config (dict): Loader configuration. Must include:
            - "loader_name": str
            - "params": dict (optional)

    Returns:
        An instance of the loader.

    Raises:
        ValueError: If 'loader_name' is missing or not found.
        TypeError: If 'params' is not a dictionary.
        Exception: If instantiating the loader fails.
    """
    loader_name = config.get("loader_name")
    if not loader_name:
        raise ValueError("Configuration must include 'loader_name'.")

    params = config.get("params", {})
    if not isinstance(params, dict):
        raise TypeError(f"'params' must be a dict, got {type(params)}")

    try:
        loader_class = get_loader(loader_name)
    except ValueError as e:
        raise ValueError(f"Loader '{loader_name}' not found: {e}")

    try:
        loader_instance = loader_class(**params)
    except Exception as e:
        raise Exception(f"Failed to instantiate loader '{loader_name}' with params {params}: {e}")

    return loader_instance
