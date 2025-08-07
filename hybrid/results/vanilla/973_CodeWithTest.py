import os
import shutil

def task_func(path, delimiter="/"):
    # Validate the input path
    if not isinstance(path, str) or not path:
        raise ValueError("The 'path' must be a non-empty string.")
    
    # Split the path by the specified delimiter
    components = path.split(delimiter)
    
    # Check for invalid components
    if any(not component for component in components):
        raise ValueError("The 'path' contains invalid components.")
    
    # Initialize the result list
    result = []
    
    # Construct the full path for each component and calculate disk usage
    current_path = ""
    for component in components:
        if current_path:
            current_path = os.path.join(current_path, component)
        else:
            current_path = component
        
        # Check if the current path exists
        if not os.path.exists(current_path):
            raise FileNotFoundError(f"The path '{current_path}' does not exist in the filesystem.")
        
        # Get disk usage statistics
        total, used, free = shutil.disk_usage(current_path)
        
        # Append the component and its disk usage to the result list
        result.append((component, {'total': total, 'used': used, 'free': free}))
    
    return result
import unittest
from collections import namedtuple
from unittest.mock import patch
import tempfile
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        DiskUsage = namedtuple("DiskUsage", ["total", "used", "free"])
        # Setup realistic disk usage values for different directories
        self.mock_usage_root = DiskUsage(500000000000, 300000000000, 200000000000)
        self.mock_usage_docs = DiskUsage(100000000000, 50000000000, 50000000000)
        self.mock_usage_src = DiskUsage(50000000000, 25000000000, 25000000000)
        self.mock_usage_home = DiskUsage(200000000000, 100000000000, 100000000000)
    def disk_usage_side_effect(self, path):
        # Helper for mocking
        if path.endswith("src"):
            return self.mock_usage_src
        elif path.endswith("Docs"):
            return self.mock_usage_docs
        elif path == "/home":
            return self.mock_usage_home
        return self.mock_usage_root
    @patch("os.path.exists")
    def test_nonexist_path(self, mock_exists):
        # Test function should raise error if path does not exist
        mock_exists.return_value = True
        with tempfile.TemporaryDirectory() as tmpdirname:
            non_exist_path = os.path.join(tmpdirname, "nonexist")
            with self.assertRaises(FileNotFoundError):
                task_func(non_exist_path)
    def test_invalid_path(self):
        # Test function should raise error if path is not valid
        with self.assertRaises(ValueError):
            task_func("")
        with self.assertRaises(ValueError):
            task_func(123)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_varied_path(self, mock_disk_usage, mock_exists):
        # Test functionality
        mock_exists.return_value = True
        mock_disk_usage.side_effect = self.disk_usage_side_effect
        result = task_func("Docs/src")
        expected = [
            (
                "Docs",
                {
                    "total": self.mock_usage_docs.total,
                    "used": self.mock_usage_docs.used,
                    "free": self.mock_usage_docs.free,
                },
            ),
            (
                "src",
                {
                    "total": self.mock_usage_src.total,
                    "used": self.mock_usage_src.used,
                    "free": self.mock_usage_src.free,
                },
            ),
        ]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_deep_nested_path(self, mock_disk_usage, mock_exists):
        # Test nested paths
        mock_exists.return_value = True
        mock_disk_usage.return_value = self.mock_usage_src
        deep_path = "Docs/src/Projects/Python/Example"
        result = task_func(deep_path)
        expected = [
            ("Docs", self.mock_usage_src._asdict()),
            ("src", self.mock_usage_src._asdict()),
            ("Projects", self.mock_usage_src._asdict()),
            ("Python", self.mock_usage_src._asdict()),
            ("Example", self.mock_usage_src._asdict()),
        ]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_single_directory(self, mock_disk_usage, mock_exists):
        # Test function works on single directory
        mock_exists.return_value = True
        mock_disk_usage.return_value = self.mock_usage_home
        result = task_func("home")
        expected = [("home", self.mock_usage_home._asdict())]
        self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_path_with_multiple_delimiters(self, mock_disk_usage, mock_exists):
        # Test should fail if there is an invalid path component
        mock_exists.return_value = True
        mock_disk_usage.side_effect = lambda path: {
            "/Docs": self.mock_usage_docs,
            "/Docs/src": self.mock_usage_src,
        }.get(path, self.mock_usage_root)
        with self.assertRaises(ValueError):
            result = task_func("Docs//src")
            expected = [
                ("Docs", self.mock_usage_docs._asdict()),
                ("", {"total": 0, "used": 0, "free": 0}),
                ("src", self.mock_usage_src._asdict()),
            ]
            self.assertEqual(result, expected)
    @patch("os.path.exists")
    @patch("shutil.disk_usage")
    def test_path_with_trailing_delimiter(self, mock_disk_usage, mock_exists):
        # Test should handle trailing delimiter
        mock_exists.return_value = True
        mock_disk_usage.side_effect = lambda path: {
            "/Docs": self.mock_usage_docs,
            "/Docs/src": self.mock_usage_src,
        }.get(path, self.mock_usage_root)
        result = task_func("Docs/src/")
        expected = [
            ("Docs", self.mock_usage_docs._asdict()),
            ("src", self.mock_usage_src._asdict()),
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)