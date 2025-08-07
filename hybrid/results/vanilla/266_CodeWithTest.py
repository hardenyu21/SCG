import os
import os.path
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    # Dictionary to store file sizes
    file_sizes = collections.defaultdict(int)

    # Walk through the directory
    for root, dirs, files in os.walk(my_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes[file_path] = file_size

    # Write the file sizes to a CSV file
    csv_file_path = os.path.join(my_path, FILE_NAME)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Path', 'File Size (bytes)'])
        for file_path, size in file_sizes.items():
            csv_writer.writerow([file_path, size])

    # Return the path of the CSV file
    return csv_file_path
import unittest
import tempfile
class TestCases(unittest.TestCase):
    def test_non_empty_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample files
            with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
                f.write('Hello')
            with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
                f.write('World')
            # Run the function
            csv_path = task_func(temp_dir)
            # Verify CSV file creation and contents
            self.assertTrue(os.path.exists(csv_path), 'CSV file not created')
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                self.assertEqual(len(rows), 3, 'Incorrect number of rows in CSV')
                self.assertEqual(rows[1][1], '5', 'Incorrect file size for file1.txt')
                self.assertEqual(rows[2][1], '5', 'Incorrect file size for file2.txt')
    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = task_func(temp_dir)
            self.assertTrue(os.path.exists(csv_path), 'CSV file not created in empty directory')
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                self.assertEqual(len(rows), 1, 'CSV file should only contain headers in empty directory')
    def test_nested_directories(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample files in nested directories
            os.makedirs(os.path.join(temp_dir, 'subdir1'))
            os.makedirs(os.path.join(temp_dir, 'subdir2'))
            with open(os.path.join(temp_dir, 'subdir1', 'file1.txt'), 'w') as f:
                f.write('Hello')
            with open(os.path.join(temp_dir, 'subdir2', 'file2.txt'), 'w') as f:
                f.write('World')
            # Run the function
            csv_path = task_func(temp_dir)
            # Verify CSV file creation and contents
            self.assertTrue(os.path.exists(csv_path), 'CSV file not created for nested directories')
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                self.assertEqual(len(rows), 3, 'Incorrect number of rows in CSV for nested directories')
                self.assertEqual(rows[1][1], '5', 'Incorrect file size for subdir1/file1.txt')
                self.assertEqual(rows[2][1], '5', 'Incorrect file size for subdir2/file2.txt')
        
    def test_single_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create sample files
            with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
                f.write('Hellooooooooooo')
            csv_path = task_func(temp_dir)
            self.assertTrue(os.path.exists(csv_path), 'CSV file not created')
    def test_large_number_of_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a large number of files
            for i in range(100):
                with open(os.path.join(temp_dir, f'file{i}.txt'), 'w') as f:
                    f.write(str(i))
            
            csv_path = task_func(temp_dir)
            self.assertTrue(os.path.exists(csv_path), 'CSV file not created for large number of files')
            with open(csv_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)
                self.assertEqual(len(rows), 101, 'Incorrect number of rows for large number of files')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)