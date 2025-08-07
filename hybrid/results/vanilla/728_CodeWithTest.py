import csv
import io

def task_func(filename='sample.csv', from_encoding='cp1251', to_encoding='utf8', delimiter=','):
    # Read the CSV file with the specified from_encoding
    with open(filename, 'r', encoding=from_encoding, newline='') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        data_list = list(reader)
    
    # Convert the list of dictionaries to a CSV string with the specified to_encoding
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data_list[0].keys(), delimiter=delimiter)
    writer.writeheader()
    writer.writerows(data_list)
    
    # Get the CSV data as a string and encode it to the specified to_encoding
    csv_data = output.getvalue()
    csv_data_encoded = csv_data.encode(to_encoding).decode(to_encoding)
    
    return data_list, csv_data_encoded
import unittest
from unittest.mock import patch, mock_open
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Example CSV data
        self.csv_data = "Name,Age\nAlice,30\nBob,25\n"
    @patch('os.path.exists', return_value=True)
    @patch('io.open')
    def test_case_1(self, mock_open, mock_exists):
        # Set up mock_open to provide the file content
        mock_file_handle = mock_open.return_value.__enter__.return_value
        mock_file_handle.read.return_value = "Name,Age\nAlice,30\nBob,25\n"
        # Run the function
        data, converted_csv = task_func('sample_1.csv', 'utf8', 'utf8', ',')
        # Check the output data
        expected_data = [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}]
        self.assertEqual(data, expected_data)
        self.assertIn("Alice", converted_csv)
        self.assertIn("Bob", converted_csv)
        # Assert that the file was opened with the correct parameters
        mock_open.assert_called_once_with('sample_1.csv', 'r', encoding='utf8')
        # Since we're working with CSV data, ensure the data is properly formatted
        # Ensure that the DictReader received the correct file handle and data
        mock_file_handle.read.assert_called_once()
    @patch('os.path.exists', return_value=True)
    @patch('io.open')
    def test_different_encoding(self, mock_open, mock_exists):
        # Simulate reading file with different encoding
        mock_open.return_value.__enter__.return_value.read.return_value = self.csv_data.encode('utf-8').decode('cp1251')
        # Run the function with the encoding details
        data, converted_csv = task_func('sample_1.csv', 'cp1251', 'utf8', ',')
        # Check that the conversion was handled properly
        self.assertIn("Alice", converted_csv)
        self.assertIn("Bob", converted_csv)
    @patch('io.open', new_callable=mock_open, read_data="Name,Age\nAlice,30\nBob,25\n")
    def test_empty_file(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = ""
        data, converted_csv = task_func('empty.csv', 'utf8', 'utf8', ',')
        self.assertEqual(data, [])
        self.assertEqual(converted_csv.strip(), "Column")  # Default column name in header
    @patch('os.path.exists', return_value=True)
    @patch('io.open')
    def test_invalid_csv_format(self, mock_open, mock_exists):
        # Simulate invalid CSV data
        mock_open.return_value.__enter__.return_value.read.return_value = "Name Age\nAlice 30\nBob 25"
        # Run the function
        data, converted_csv = task_func('invalid.csv', 'utf8', 'utf8', ' ')
        # Validate that data was parsed considering space as a delimiter
        self.assertTrue(all('Name' in entry and 'Age' in entry for entry in data))
    @patch('io.open', new_callable=mock_open, read_data="Name,Age\n")
    def test_csv_with_only_headers(self, mock_open):
        data, converted_csv = task_func('headers_only.csv', 'utf8', 'utf8', ',')
        self.assertEqual(data, [])
        self.assertIn("Name,Age\n", converted_csv)  # Test with normalized newline


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)