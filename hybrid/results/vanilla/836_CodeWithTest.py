import os
import shutil
import csv

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    result = {}
    
    # Ensure the processed directory exists if not in simulate mode
    if not simulate and not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Iterate over all files in the CSV directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(csv_dir, filename)
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for index, row in enumerate(reader):
                    if row and row[0] == target_value:
                        result[filename] = index
                        break
    
    # Move processed files to the processed directory if not in simulate mode
    if not simulate:
        for filename in result:
            src_path = os.path.join(csv_dir, filename)
            dst_path = os.path.join(processed_dir, filename)
            shutil.move(src_path, dst_path)
    
    return result

# Example usage:
# result = task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
# print(result)
import unittest
from unittest.mock import patch
import tempfile
import shutil
import os
from unittest.mock import mock_open, patch, MagicMock
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Common setup for all tests
        self.target_value = '332'
        self.csv_dir = '/fake/csv_files/'
        self.processed_dir = '/fake/processed_files/'
        self.simulate = True
    @patch('os.listdir', return_value=['file_with_target.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="332,Data\n333,More Data\n")
    @patch('shutil.move')
    def test_file_with_target(self, mock_move, mock_open, mock_listdir):
        """ Test case for files with the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertIn('file_with_target.csv', result)
        self.assertEqual(result['file_with_target.csv'], 0)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_without_target.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="334,Data\n335,More Data\n")
    @patch('shutil.move')
    def test_file_without_target(self, mock_move, mock_open, mock_listdir):
        """ Test case for files without the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertNotIn('file_without_target.csv', result)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['empty_file.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="")
    @patch('shutil.move')
    def test_empty_file(self, mock_move, mock_open, mock_listdir):
        """ Test case for an empty CSV file. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertNotIn('empty_file.csv', result)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_with_multiple_targets.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="332,Data\n332,More Data\n333,Other Data\n")
    @patch('shutil.move')
    def test_file_with_multiple_targets(self, mock_move, mock_open, mock_listdir):
        """ Test case for files with multiple occurrences of the target value. """
        result = task_func(target_value=self.target_value, csv_dir=self.csv_dir,
                       processed_dir=self.processed_dir, simulate=self.simulate)
        self.assertIn('file_with_multiple_targets.csv', result)
        self.assertEqual(result['file_with_multiple_targets.csv'], 0)
        mock_move.assert_not_called()
    @patch('os.listdir', return_value=['file_with_target_not_first.csv'])
    @patch('builtins.open', new_callable=mock_open, read_data="333,Data\n334,332\n335,Data\n")
    @patch('shutil.move')
    def test_file_with_target_not_first(self, mock_move, mock_open, mock_listdir):
        """ Test case for a file where the target value is not in the first cell. """
        result = task_func(target_value='332', csv_dir=self.csv_dir,
                    processed_dir=self.processed_dir, simulate=self.simulate)
        # This file should not be in the results because '332' is not in the first cell
        self.assertNotIn('file_with_target_not_first.csv', result)
        mock_move.assert_not_called()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)