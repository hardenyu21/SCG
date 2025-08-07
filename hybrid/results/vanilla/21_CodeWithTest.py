import psutil
import platform

def task_func():
    # Get the operating system name
    os_name = platform.system()
    
    # Get the system architecture
    architecture = platform.architecture()[0]
    
    # Get memory details
    memory_info = psutil.virtual_memory()
    used_memory_percentage = (memory_info.used / memory_info.total) * 100
    
    # Format the memory usage percentage
    memory_usage = f"{used_memory_percentage:.2f}%"
    
    # Return the gathered details in a dictionary
    return {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': memory_usage
    }

# Example usage
if __name__ == "__main__":
    system_details = task_func()
    print(system_details)
import unittest
class TestCases(unittest.TestCase):
    
    def test_presence_OS(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = task_func()
        self.assertTrue('OS' in result and isinstance(result['OS'], str))
    def test_presence_architecture(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = task_func()
        self.assertTrue('Architecture' in result and isinstance(result['Architecture'], str))
    def test_presence_memory_usage(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = task_func()
        self.assertTrue('Memory Usage' in result and isinstance(result['Memory Usage'], str))
    def test_return_type(self):
        """Test that the result has the correct keys and that each key maps to the expected data type."""
        result = task_func()
        self.assertIsInstance(result, dict)
    def test_memory_usage_format(self):
        """Test that the 'Memory Usage' key is correctly formatted as a percentage."""
        result = task_func()
        self.assertRegex(result['Memory Usage'], r"\d{1,3}\.\d{2}%")
    
    def test_non_empty_values(self):
        """Ensure that the values associated with each key are non-empty."""
        result = task_func()
        for key, value in result.items():
            self.assertTrue(bool(value))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)