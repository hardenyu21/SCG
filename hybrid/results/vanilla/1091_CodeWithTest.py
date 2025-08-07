import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def task_func(directory):
    # List to store the dictionaries extracted from the text files
    dictionaries = []
    
    # Get all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in text_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
            try:
                # Attempt to parse the content as a dictionary
                parsed_dict = ast.literal_eval(content)
                
                # Check if the parsed content is indeed a dictionary
                if isinstance(parsed_dict, dict):
                    dictionaries.append(parsed_dict)
                else:
                    raise ValueError(f"Invalid dictionary representation in file: {file_path}")
            
            except (ValueError, SyntaxError) as e:
                # Raise an exception if the content is not a valid dictionary
                raise ValueError(f"Invalid dictionary representation in file: {file_path}") from e
    
    return dictionaries

# Example usage:
# dictionaries = task_func(DIRECTORY)
# print(dictionaries)
import unittest
import os
import ast
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_task_func'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_task_func/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory+"/1.txt","w")
        f.write("{'key1': 'value1'}")
        f.close()
        f = open(self.sample_directory+"/2.txt","w")
        f.write("{'key2': 'value2', 'key3': 'value3'}")
        f.close()
        f = open(self.sample_directory+"/3.txt","w")
        f.write("{'key4': 'value4'}")
        f.close()
        f = open(self.sample_directory+"/4.txt","w")
        f.write("{'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}")
        f.close()
        f = open(self.sample_directory+"/5.txt","w")
        f.write("{'key8': 'value8'}")
        f.close()
        self.empty_directory = "testdir_task_func/empty_directory"
        os.makedirs(self.empty_directory, exist_ok=True)
        self.multi_line_directory = "testdir_task_func/multi_line_directory"
        os.makedirs(self.multi_line_directory, exist_ok=True)
        f = open(self.multi_line_directory+"/1.txt","w")
        f.write("{'key1': 'value1'}\n{'key2': 'value2'}")
        f.close()
        self.mixed_directory = "testdir_task_func/mixed_directory"
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        self.invalid_directory = "testdir_task_func/invalid_directory"
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        f = open(self.invalid_directory+"/2.txt","w")
        f.write("{'key1': 'value1'}")
        f.close()
    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Test with the sample directory
        result = task_func(self.sample_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2', 'key3': 'value3'},
            {'key4': 'value4'},
            {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'},
            {'key8': 'value8'}
        ]
        for i in expected_result:
            self.assertTrue(i in result)
        
    def test_case_2(self):
        # Test with an empty directory
        result = task_func(self.empty_directory)
        self.assertEqual(result, [])
        
    def test_case_3(self):
        # Test with a directory containing a text file without valid dictionary representation
        with self.assertRaises(ValueError):
            task_func(self.invalid_directory)
            
    def test_case_4(self):
        # Test with a directory containing multiple text files, some of which are invalid
        with self.assertRaises(ValueError):
            task_func(self.mixed_directory)
            
    def test_case_5(self):
        # Test with a directory containing a text file with multiple valid dictionary representations
        result = task_func(self.multi_line_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2'}
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)