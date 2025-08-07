from texttable import Texttable
import psutil

def task_func():
    # Create a new Texttable object
    table = Texttable()
    
    # Set the header for the table
    table.set_cols_align(["l", "r"])
    table.set_cols_valign(["m", "m"])
    table.add_rows([["Item", "Value"]])
    
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Get memory usage percentage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    
    # Get disk usage percentage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    
    # Add rows to the table with the system information
    table.add_rows([
        ["CPU Usage (%)", f"{cpu_usage}%"],
        ["Memory Usage (%)", f"{memory_usage}%"],
        ["Disk Usage (%)", f"{disk_usage}%"]
    ])
    
    # Return the string representation of the table
    return table.draw()

# Example usage
if __name__ == "__main__":
    print(task_func())
import unittest
import re  # Import the regular expressions library
class TestCases(unittest.TestCase):
    def setUp(self):
        self.result = task_func()
    def test_return_type(self):
        """Test that the function returns a string."""
        self.assertIsInstance(self.result, str)
    def test_table_headers(self):
        """Test the presence of correct headers in the table."""
        for header in ['CPU Usage (%)', 'Memory Usage (%)', 'Disk Usage (%)']:
            with self.subTest(header=header):
                self.assertIn(header, self.result)
    def test_proper_values(self):
        """Test that the table's values are not empty or zero."""
        # Extract numeric values using a regular expression
        values = re.findall(r'\|\s*[\d.]+\s*\|', self.result)
        # Convert extracted strings to float and test they are greater than 0
        for value_str in values:
            value = float(value_str.strip('| ').strip())
            with self.subTest(value=value):
                self.assertTrue(0 <= value <= 100)
    def test_value_ranges(self):
        """Test that CPU and memory usage percentages are within 0-100%."""
        values = re.findall(r'\|\s*[\d.]+\s*\|', self.result)
        for value_str in values:
            value = float(value_str.strip('| ').strip())
            with self.subTest(value=value):
                self.assertTrue(0 <= value <= 100)
    def test_table_structure(self):
        """Test that the table's structure is as expected."""
        # Split the table into rows based on the unique row separator pattern
        parts = self.result.split('+------------------+--------+')
        # Filter out empty parts that might occur due to the split operation
        non_empty_parts = [part for part in parts if part.strip()]
        # Expect 4 non-empty parts: 1 header row + 3 data rows
        self.assertTrue(1 <= len(non_empty_parts) <= 3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)