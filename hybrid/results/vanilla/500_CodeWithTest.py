import xlwt
import os

# Constants
FIELDS = ['ID', 'Name', 'Age']

def task_func(values, filename):
    # Create a new workbook and add a worksheet
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    
    # Write the header row
    for col_index, field in enumerate(FIELDS):
        worksheet.write(0, col_index, field)
    
    # Write the data rows
    for row_index, row_data in enumerate(values, start=1):
        for col_index, field in enumerate(FIELDS):
            worksheet.write(row_index, col_index, row_data.get(field, ''))
    
    # Save the workbook to the specified filename
    workbook.save(filename)
    
    # Return the absolute path of the created file
    return os.path.abspath(filename)

# Example usage
empty_data = []
path = task_func(empty_data, 'empty_data.xls')
print(os.path.exists(path) and 'empty_data.xls' in path)  # Should print True
import unittest
import os
import tempfile
from collections import OrderedDict
# Assume task_func is imported or defined elsewhere
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store test files
        self.test_dir = tempfile.TemporaryDirectory()
    def tearDown(self):
        # Cleanup the temporary directory after tests
        self.test_dir.cleanup()
    def test_ordered_dict_to_excel(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)]),
                  OrderedDict([('ID', 2), ('Name', 'Jane Doe'), ('Age', 28)])]
        filename = os.path.join(self.test_dir.name, 'test_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_empty_data_to_excel(self):
        values = []
        filename = os.path.join(self.test_dir.name, 'empty_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_incomplete_data_to_excel(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe')])]
        filename = os.path.join(self.test_dir.name, 'incomplete_data.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_mismatched_fields(self):
        values = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Gender', 'Male')])]
        filename = os.path.join(self.test_dir.name, 'mismatched_fields.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))
    def test_multiple_rows(self):
        values = [OrderedDict([('ID', i), ('Name', f'Name {i}'), ('Age', 20+i)]) for i in range(5)]
        filename = os.path.join(self.test_dir.name, 'multiple_rows.xls')
        result_path = task_func(values, filename)
        self.assertTrue(os.path.isfile(result_path))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)