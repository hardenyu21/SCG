import os
import logging

def task_func(directory):
    # Set up logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO, 
                        format='%(asctime)s - %(message)s')
    
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Initialize counters and list for removed files
    files_removed = 0
    removed_files_list = []
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JavaScript file containing 'jquery' in its name
        if filename.lower().endswith('.js') and 'jquery' in filename.lower():
            file_path = os.path.join(directory, filename)
            try:
                # Remove the file
                os.remove(file_path)
                # Log the removal
                logging.info(f"Removed file: {file_path}")
                # Update counters and list
                files_removed += 1
                removed_files_list.append(filename)
            except Exception as e:
                # Log any errors that occur during file removal
                logging.error(f"Error removing file {file_path}: {e}")
    
    # Return the result as a tuple
    return files_removed, removed_files_list
import unittest
from unittest.mock import MagicMock, patch
class TestCases(unittest.TestCase):
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('os.remove')
    def test_remove_jquery_files(self, mock_remove, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js', 'otherfile.txt', 'example.js']
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 3)
        self.assertListEqual(removed_files, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])
    @patch('os.path.exists')
    @patch('os.listdir')
    def test_empty_directory(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        removed_count, removed_files = task_func('/fake/empty/directory')
        self.assertEqual(removed_count, 0)
        self.assertListEqual(removed_files, [])
    @patch('os.path.exists')
    def test_nonexistent_directory(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            task_func('/fake/nonexistent/directory')
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.min.js', 'jquery-ui.css'])
    @patch('os.remove')
    def test_remove_jquery_files_not_js(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 2)
        self.assertListEqual(removed_files, ['jquery-1.js', 'jquery-2.min.js'])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['subdir', 'jquery-1.js'])
    @patch('os.remove')
    def test_remove_jquery_files_subdirectory(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 1)
        self.assertListEqual(removed_files, ['jquery-1.js'])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])
    @patch('os.remove', side_effect=OSError("Permission denied"))
    def test_remove_jquery_files_error(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 0)
        self.assertListEqual(removed_files, [])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.min.js', 'jquery-ui.css'])
    @patch('os.remove')
    def test_logging(self, mock_remove, mock_listdir, mock_exists):
        """Test if logging works as expected."""
        with patch('logging.info') as mock_info, \
             patch('logging.error') as mock_error:
            task_func('/fake/directory')
            mock_info.assert_called()
            mock_error.assert_not_called()  # Ensure that no error message is logged
    def tearDown(self):
        """Remove the generated log file after each test."""
        log_file = 'jquery_removal.log'
        if os.path.exists(log_file):
            logging.shutdown()  # Manually close the logging file handler
            os.remove(log_file)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)