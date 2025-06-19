import os

def validate_path(path: str, must_be_file: bool = False, must_be_dir: bool = False):
    """
    Validate the existence and type of a given path.

    Args:
        path (str): The path to validate.
        must_be_file (bool): If True, the path must be a file.
        must_be_dir (bool): If True, the path must be a directory.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If the path type does not match expectations.
        PermissionError: If the path is not readable.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path not found: {path}")

    if must_be_file and not os.path.isfile(path):
        raise ValueError(f"Path is not a file: {path}")

    if must_be_dir and not os.path.isdir(path):
        raise ValueError(f"Path is not a directory: {path}")

    if not os.access(path, os.R_OK):
        raise PermissionError(f"Read access denied for path: {path}")
