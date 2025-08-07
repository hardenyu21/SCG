import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')
    
    # Define invalid characters
    invalid_chars = set('<>:"|?*')
    
    # Check for invalid characters
    if any(char in invalid_chars for char in path):
        raise ValueError("The path contains invalid characters.")
    
    # Split the path into components using the specified delimiter
    components = path.split(delimiter)
    
    return components
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing a standard UNIX-like path with '/' delimiter
        self.assertEqual(
            task_func("Docs/src/Scripts/temp", "/"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_2(self):
        # Testing a standard Windows-like path with '\' delimiter
        self.assertEqual(
            task_func("Docs\\src\\Scripts\\temp", "\\"),
            ["Docs", "src", "Scripts", "temp"],
        )
    def test_case_3(self):
        # Testing an empty path string
        self.assertEqual(task_func("", "/"), [])
    def test_case_4(self):
        # Testing a path with invalid characters
        self.assertEqual(task_func("Docs/src/Scripts|temp", "/"), [])
    def test_case_5(self):
        # Testing a path with a different delimiter
        self.assertEqual(task_func("Docs|src|Scripts|temp", "|"), [])
    def test_case_6(self):
        # Handle leading and trailing delimiters
        self.assertEqual(task_func("/Docs/src/Scripts/", "/"), ["Docs", "src", "Scripts"])
    def test_case_7(self):
        # Test mixed delimiters given expected conversion
        self.assertEqual(
            task_func("Docs/src\\Scripts/temp", "\\"), ["Docs", "src", "Scripts", "temp"]
        )
        self.assertEqual(
            task_func("Docs/src\\Scripts/temp", "/"), ["Docs", "src", "Scripts", "temp"]
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)