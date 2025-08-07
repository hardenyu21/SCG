import os
import json

def task_func(config_path: str) -> dict:
    """
    Load a JSON configuration file and return the configuration dictionary.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        dict: Configuration dictionary loaded from the file.

    Raises:
        FileNotFoundError: If the provided configuration file does not exist.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file '{config_path}' does not exist.")
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config