import os
from collections import Counter

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise OSError(f"The specified directory '{directory}' does not exist.")
    
    # Initialize a Counter object to store the counts of each file extension
    file_counter = Counter()
    
    # Walk through the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            # Get the file extension
            file_extension = os.path.splitext(file)[1]
            
            # Check if the file extension is in the specified extensions
            if file_extension in extensions:
                # Increment the count for this file extension
                file_counter[file_extension] += 1
    
    # If keep_zero is False, remove extensions with zero count
    if not keep_zero:
        file_counter = Counter({ext: count for ext, count in file_counter.items() if count > 0})
    
    return file_counter
import unittest
from collections import Counter
from tempfile import TemporaryDirectory
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
    def tearDown(self):
        self.temp_dir.cleanup()
    def create_test_files(self, directory, file_list):
        for file_name in file_list:
            with open(os.path.join(directory, file_name), "w") as f:
                f.write("Test")
    def test_case_1(self):
        # Test basic case with default extensions
        file_names = ["file1.txt", "file2.docx", "file3.xlsx", "file4.csv", "file5.txt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 2, ".docx": 1, ".xlsx": 1, ".csv": 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test empty directory
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 0, ".docx": 0, ".xlsx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_3(self):
        # Test error handling - non-existent directory
        with self.assertRaises(OSError):
            task_func("/path/to/nonexistent/directory")
    def test_case_4(self):
        # Test ignoring unspecified extensions
        file_names = ["file1.pdf", "file2.png", "file3.txt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 1, ".docx": 0, ".xlsx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_5(self):
        # Test nested folders
        nested_dir_path = os.path.join(self.temp_dir.name, "nested")
        os.makedirs(nested_dir_path)
        file_names = ["nested_file1.txt", "nested_file2.xlsx"]
        self.create_test_files(nested_dir_path, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 1, ".xlsx": 1, ".docx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_6(self):
        # Test custom extensions
        file_names = ["image.jpeg", "video.mp4", "document.pdf"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(
            self.temp_dir.name, extensions=[".jpeg", ".mp4"], keep_zero=False
        )
        expected = Counter({".jpeg": 1, ".mp4": 1})
        self.assertEqual(result, expected)
    def test_case_7(self):
        # Test custom extensions
        file_names = ["file1.txt", "file2.docx"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name, keep_zero=False)
        expected = Counter(
            {".txt": 1, ".docx": 1}
        )  # .xlsx and .csv are omitted because their count is 0 and keep_zero is False
        self.assertEqual(result, expected)
    def test_case_8(self):
        # Test case sensitivity
        file_names = ["file1.txt", "file1.tXt", "fiLE.txt", "fiLE.TXt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name, extensions=[".txt"])
        expected = Counter({".txt": 2})
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)