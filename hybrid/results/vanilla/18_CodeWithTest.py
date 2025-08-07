import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if the file exists and is a CSV file
    if not os.path.isfile(file) or not file.endswith('.csv'):
        return []

    try:
        # Use the 'split' command to divide the CSV file into smaller files
        # Each file will have a prefix 'split_'
        subprocess.run(['split', '-l', '100', file, 'split_'], check=True)

        # Get a list of all split files
        split_files = glob.glob('split_*')

        # Shuffle the lines in each split file
        for split_file in split_files:
            with open(split_file, 'r', newline='') as f:
                reader = csv.reader(f)
                lines = list(reader)

            random.shuffle(lines)

            with open(split_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(lines)

        return split_files

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while splitting the file: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
import unittest
import csv
import os
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to hold the files
        self.test_dir = tempfile.mkdtemp()
        self.small_csv_path = os.path.join(self.test_dir, "small.csv")
        self.medium_csv_path = os.path.join(self.test_dir, "medium.csv")
        self.large_csv_path = os.path.join(self.test_dir, "large.csv")
        self.non_csv_path = os.path.join(self.test_dir, "test.txt")
        
        # Create dummy CSV files of different sizes
        with open(self.small_csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(10):  # Small CSV
                writer.writerow([f"row{i}", f"value{i}"])
        
        with open(self.medium_csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(100):  # Medium CSV
                writer.writerow([f"row{i}", f"value{i}"])
        
        with open(self.large_csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(1000):  # Large CSV
                writer.writerow([f"row{i}", f"value{i}"])
        
        # Create a non-CSV file
        with open(self.non_csv_path, "w") as file:
            file.write("This is a test text file.")
    def tearDown(self):
        # Remove all files created in the directory
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)  # Remove each file
    def test_small_csv(self):
        """Test splitting and shuffling a small CSV file."""
        split_files = task_func(self.small_csv_path)
        self.assertTrue(len(split_files) > 0, "No files were split.")
        self.assertNotEqual(self._read_csv(self.small_csv_path), self._read_csv(split_files[0]), "Rows are not shuffled.")
        for filename in split_files:
            os.remove(filename)
    def test_medium_csv(self):
        """Test splitting and shuffling a medium CSV file."""
        split_files = task_func(self.medium_csv_path)
        self.assertTrue(len(split_files) > 0, "No files were split.")
        self.assertNotEqual(self._read_csv(self.medium_csv_path), self._read_csv(split_files[0]), "Rows are not shuffled.")
        for filename in split_files:
            os.remove(filename)
    def test_large_csv(self):
        """Test splitting and shuffling a large CSV file."""
        split_files = task_func(self.large_csv_path)
        self.assertTrue(len(split_files) > 0, "No files were split.")
        self.assertNotEqual(self._read_csv(self.large_csv_path), self._read_csv(split_files[0]), "Rows are not shuffled.")
        for filename in split_files:
            os.remove(filename)
    def test_invalid_file(self):
        """Test behavior with a non-existent file path."""
        split_files = task_func("/path/that/does/not/exist.csv")
        self.assertEqual(split_files, [], "Expected an empty list for an invalid file path.")
    def test_non_csv_file(self):
        """Test behavior with a non-CSV file."""
        split_files = task_func(self.non_csv_path)
        self.assertEqual(split_files, [], "Expected an empty list for a non-CSV file.")
    def _read_csv(self, filepath):
        """Helper method to read CSV file and return content."""
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            return list(reader)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)