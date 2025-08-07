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
import unittest
from unittest.mock import patch, MagicMock
import sys
class TestCases(unittest.TestCase):
    @patch('importlib.import_module')
    @patch('pkgutil.iter_modules')
    def test_package_module_addition(self, mock_iter_modules, mock_import_module):
        # Create a mock for the package with a __path__ attribute as a list
        package_mock = MagicMock()
        package_mock.__path__ = ['mocked_path']  # Ensure this is a list
        # Configure import_module to return the package mock when any module name is passed
        mock_import_module.return_value = package_mock
        # Setup the mock for iter_modules to simulate finding modules in a package
        mock_iter_modules.return_value = [
            (None, 'module1', True),  # Simulate a package has 'module1'
            (None, 'module2', True)  # Simulate a package has 'module2'
        ]
        # Call the function under test
        modules_added = task_func('numpy')
        # Perform your assertions here
        # For example, assert that modules were "added" (imported)
        self.assertFalse(len(modules_added) > 0)
    def test_nonexistent_package(self):
        with self.assertRaises(ImportError):
            task_func('nonexistentpkg')
    def test_empty_package(self):
        try:
            modules_added = task_func('empty_package')
            self.assertEqual(len(modules_added), 0)
        except ImportError:
            self.assertTrue(True, "Package not found, which is expected in this test.")
    def test_module_path_in_sys_path(self):
        # Assuming 'numpy' is installed
        modules_added = task_func('numpy')
        for module in modules_added:
            self.assertTrue(any(module in path for path in sys.path))
    def test_no_duplicates_in_sys_path(self):
        # Assuming 'numpy' is installed
        modules_added = task_func('numpy')
        for module in modules_added:
            self.assertEqual(sum(module in path for path in sys.path), 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)