import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    # Ensure the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List to store the names of files that were moved
    moved_files = []

    # Iterate over all files in the source directory
    for filename in os.listdir(source_directory):
        # Check if the filename matches the pattern
        if fnmatch.fnmatch(filename, file_pattern):
            # Construct full file paths
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_directory, filename)

            # Move the file
            shutil.move(source_file, destination_file)

            # Add the filename to the list of moved files
            moved_files.append(filename)

    # Return the list of moved files
    return moved_files
import unittest
from unittest.mock import patch, MagicMock, call
import shutil
import os
import fnmatch
class TestCases(unittest.TestCase):
    def setUp(self):
        self.source_directory = "/fake/source_directory"
        self.destination_directory = "/fake/destination_directory"
        self.files = ['file1.txt', 'file2.txt', 'image.jpg', 'data.log', 'report.TXT', 'config file.cfg']
    @patch('os.walk')
    @patch('shutil.move')
    def test_no_files_to_move(self, mock_move, mock_walk):
        mock_walk.return_value = [(self.source_directory, [], ['image.jpg', 'data.log', 'config file.cfg'])]
        result = task_func(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(result, [])
        mock_move.assert_not_called()
    @patch('os.walk')
    @patch('shutil.move')
    def test_non_existing_source_directory(self, mock_move, mock_walk):
        mock_walk.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func('/non/existing/directory', self.destination_directory, '*.txt')
    @patch('os.walk')
    @patch('shutil.move')
    def test_case_sensitivity(self, mock_move, mock_walk):
        # Setting up os.walk to simulate case sensitivity in file matching
        mock_walk.return_value = [
            (self.source_directory, [], ['file1.txt', 'file2.TXT', 'report.TXT'])
        ]
        # Execute the function
        task_func(self.source_directory, self.destination_directory, '*.TXT')
        expected_calls = [
            call(os.path.join(self.source_directory, 'file2.TXT'), os.path.join(self.destination_directory, 'file2.TXT')),
            call(os.path.join(self.source_directory, 'report.TXT'), os.path.join(self.destination_directory, 'report.TXT'))
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)
    @patch('os.walk')
    @patch('shutil.move')
    def test_special_characters_in_filenames(self, mock_move, mock_walk):
        mock_walk.return_value = [(self.source_directory, [], ['config file.cfg'])]
        task_func(self.source_directory, self.destination_directory, '*.cfg')
        expected_call = call(os.path.join(self.source_directory, 'config file.cfg'), os.path.join(self.destination_directory, 'config file.cfg'))
        mock_move.assert_has_calls([expected_call], any_order=True)
    @patch('os.listdir')
    @patch('shutil.move')
    @patch('os.path.exists')
    def test_no_matching_files(self, mock_exists, mock_move, mock_listdir):
        # Setup mocks to simulate no matching files
        mock_listdir.return_value = ['file3.jpg']
        mock_exists.return_value = True
        # Call the function
        moved_files = task_func(self.source_directory, self.destination_directory, '*.txt')
        # Assertions
        mock_move.assert_not_called()
        self.assertEqual(moved_files, [], "No TXT files should be moved")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)