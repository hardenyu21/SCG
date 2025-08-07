import os
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    # Ensure the log directory exists
    if not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir)
        except OSError as e:
            print(f"Error creating directory {log_dir}: {e}")
            return False

    # Construct the full file path
    file_path = os.path.join(log_dir, filename)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Prepare the log entry
    log_entry = f"{timestamp} - Metrics: {metrics}\n"

    try:
        # Open the file in append mode and write the log entry
        with open(file_path, 'a') as file:
            file.write(log_entry)
        return True
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")
        return False

# Example usage
metrics = {'precision': 0.75, 'recall': 0.80}
success = task_func(metrics, 'evaluation.log')
print(success)
import unittest
from unittest.mock import patch, mock_open, MagicMock
class TestCases(unittest.TestCase):
    def setUp(self):
        self.metrics = {'accuracy': 0.98, 'loss': 0.05}
        self.filename = 'metrics.log'
        self.log_dir = './temp_logs'
    def test_non_string_filename(self):
        with self.assertRaises(ValueError):
            task_func(self.metrics, 12345, log_dir=self.log_dir)
    def test_non_dictionary_metrics(self):
        with self.assertRaises(ValueError):
            task_func('accuracy: 0.95', self.filename, log_dir=self.log_dir)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_normal_metrics_logging(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir=self.log_dir)
        self.assertTrue(result)
        mock_file.assert_called_once_with(os.path.join(self.log_dir, self.filename), 'a')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=True)
    def test_normal_metrics_logging(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir=self.log_dir)
        self.assertTrue(result)
        mock_file.assert_called_once_with(os.path.join(self.log_dir, self.filename), 'a')
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_non_existent_log_directory(self, mock_exists, mock_file, mock_makedirs):
        result = task_func(self.metrics, self.filename, log_dir='./nonexistent_dir')
        self.assertTrue(result)
    @patch('os.makedirs')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('os.path.exists', return_value=True)
    def test_empty_metrics(self, mock_exists, mock_open, mock_makedirs):
        # Setup the mock file handle that open returns
        mock_file_handle = mock_open.return_value.__enter__.return_value
        
        # Call the function
        metrics = {}
        filename = 'empty_metrics.log'
        log_dir = './temp_logs'
        result = task_func(metrics, filename, log_dir=log_dir)
        # Assert that the function returned True for successful logging
        self.assertTrue(result)
        # Check that 'write' was called exactly twice: once for the timestamp, once for the newline
        self.assertEqual(mock_file_handle.write.call_count, 2)
        # Check that the calls were for writing the timestamp and an empty line
        args_list = mock_file_handle.write.call_args_list
        self.assertTrue(args_list[0][0][0].endswith('\n'))  # Check if first write is a timestamp ending with newline
        self.assertEqual(args_list[1][0][0], '\n')  # Check if second write is just a newline
    def test_non_string_filename(self):
        with self.assertRaises(ValueError):
            task_func(self.metrics, 12345, log_dir=self.log_dir)
    def test_non_dictionary_metrics(self):
        with self.assertRaises(ValueError):
            task_func('accuracy: 0.95', self.filename, log_dir=self.log_dir)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)