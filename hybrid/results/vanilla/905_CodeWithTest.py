import os
import glob

def task_func(directory_path, file_extension='.csv'):
    # Initialize an empty dictionary to store the data
    data = {}
    
    # Construct the search pattern for files with the specified extension
    search_pattern = os.path.join(directory_path, f'*{file_extension}')
    
    # Use glob to find all files matching the pattern
    for file_path in glob.glob(search_pattern):
        # Extract the filename without the extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Initialize a list to store the rows of the file
        rows = []
        
        # Open the file and read its contents
        with open(file_path, 'r', newline='') as file:
            # Use csv.reader to read the file, assuming comma as the delimiter
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        
        # Add the file's data to the dictionary
        data[file_name] = rows
    
    return data
import unittest
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # create a directory with test files
        os.mkdir('test_1')
        with open('test_1/file1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])
        os.mkdir('test_2')
        with open('test_2/file2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['name', 'age'], ['Alice', '30'], ['Bob', '40']])
        os.mkdir('test_5')
        with open('test_5/file3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([['subject', 'marks'], ['Math', '90'], ['Science', '85']])
    def tearDown(self):
        # remove the test directories
        shutil.rmtree('test_1')
        shutil.rmtree('test_2')
        shutil.rmtree('test_5')
    
    def test_case_1(self):
        # This test assumes the existence of a directory named 'task_func_data' with a CSV file 'file1.csv'
        data = task_func('test_1')
        self.assertIsInstance(data, dict)
        self.assertIn('file1', data)
        self.assertEqual(data['file1'], [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']])
    def test_case_2(self):
        # This test checks explicit file_extension input
        data = task_func('test_2', '.csv')
        self.assertIsInstance(data, dict)
        self.assertIn('file2', data)
        self.assertEqual(data['file2'], [['name', 'age'], ['Alice', '30'], ['Bob', '40']])
    def test_case_3(self):
        # This test checks for a non-existent file extension, expecting an empty dictionary
        data = task_func('test_3', '.txt')
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)
    def test_case_4(self):
        # This test checks for a non-existent directory, expecting an empty dictionary
        data = task_func('/nonexistent/directory')
        self.assertIsInstance(data, dict)
        self.assertEqual(len(data), 0)
    def test_case_5(self):
        # This test checks another file's presence and content in the dictionary
        data = task_func('test_5')
        self.assertIsInstance(data, dict)
        self.assertIn('file3', data)
        self.assertEqual(data['file3'], [['subject', 'marks'], ['Math', '90'], ['Science', '85']])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)