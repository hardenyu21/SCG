import os
import sys
import importlib
from pkgutil import iter_modules

def task_func(package_name):
    try:
        # Attempt to import the package to check if it's installed
        package = importlib.import_module(package_name)
    except ImportError:
        # Raise an ImportError with a message to install the package
        raise ImportError(f"Package '{package_name}' is not installed. Please install it using: pip install {package_name}")

    # Get the package path
    package_path = package.__path__

    # List to store module names that are added to the system path
    added_modules = []

    # Iterate over all modules in the package
    for _, module_name, is_pkg in iter_modules(package_path):
        # Construct the full module name
        full_module_name = f"{package_name}.{module_name}"

        # Check if the module is not already in the system path
        if full_module_name not in sys.modules:
            # Add the module to the system path
            sys.modules[full_module_name] = importlib.import_module(full_module_name)
            added_modules.append(full_module_name)

    return added_modules