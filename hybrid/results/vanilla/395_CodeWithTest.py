import re
import os
import glob
import natsort
import pandas as pd

def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The specified directory '{directory}' does not exist.")
    
    # Find all files matching the pattern
    file_paths = glob.glob(os.path.join(directory, file_pattern))
    
    # Sort the file paths naturally
    file_paths = natsort.natsorted(file_paths)
    
    # Check if any files were found
    if not file_paths:
        raise ValueError(f"No files matching the pattern '{file_pattern}' were found in the directory '{directory}'.")
    
    # Prepare a list to store the extracted data
    data = []
    
    # Compile the regex pattern
    pattern = re.compile(regex)
    
    # Iterate over each file
    for file_path in file_paths:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all numeric data in the file
        numeric_data = pattern.findall(content)
        
        # Convert numeric data to integers
        numeric_data = [int(num) for num in numeric_data]
        
        # Append the filename and numeric data to the list
        data.append({'Filename': os.path.basename(file_path), 'Numeric Data': numeric_data})
    
    # Create a DataFrame from the collected data
    df = pd.DataFrame(data)
    
    return df
import unittest
import pandas as pd
import os
def create_dummy_files(data_dir):
    os.makedirs(data_dir, exist_ok=True)
    # Creating test files
    test_files_data = {
        'file1.txt': '123 abc 456',
        'file2.txt': '789 xyz',
        'empty.txt': '',
        'non_numeric.txt': 'abc def',
        'mixed.txt': 'abc 123 def 456'
    }
    for filename, content in test_files_data.items():
        with open(data_dir + filename, 'w') as file:
            file.write(content)
def tear_down_files(data_dir):
    for filename in os.listdir(data_dir):
        os.remove(os.path.join(data_dir, filename))
    os.rmdir(data_dir)
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = './test_data/'
        os.makedirs(self.test_data_dir, exist_ok=True)
        # Creating test files
        test_files_data = {
            'file1.txt': '123 abc 456',
            'file2.txt': '789 xyz',
            'empty.txt': '',
            'non_numeric.txt': 'abc def',
            'mixed.txt': 'abc 123 def 456'
        }
        for filename, content in test_files_data.items():
            with open(self.test_data_dir + filename, 'w') as file:
                file.write(content)
    def tearDown(self):
        for filename in os.listdir(self.test_data_dir):
            os.remove(os.path.join(self.test_data_dir, filename))
        os.rmdir(self.test_data_dir)
    def test_normal_functionality(self):
        df = task_func(self.test_data_dir)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 5)  # Number of files
        self.assertIn('123', df.loc[df['Filename'] == 'file1.txt', 'Numeric Data'].values[0])
        df_list = df.apply(lambda row: ','.join(str(e) for e in row), axis=1).tolist()
        # Write the DataFrame to a file for inspection
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
        expect = ['empty.txt,[]', "file1.txt,['123', '456']", "file2.txt,['789']", "mixed.txt,['123', '456']", 'non_numeric.txt,[]']
        self.assertEqual(df_list, expect)
    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./nonexistent_directory/')
    def test_no_matching_files(self):
        with self.assertRaises(ValueError):
            task_func(self.test_data_dir, '*.csv')
    def test_empty_file(self):
        df = task_func(self.test_data_dir)
        self.assertEqual([], df.loc[df['Filename'] == 'empty.txt', 'Numeric Data'].values[0])
    def test_mixed_content_file(self):
        df = task_func(self.test_data_dir)
        self.assertIn('123', df.loc[df['Filename'] == 'mixed.txt', 'Numeric Data'].values[0])
        self.assertIn('456', df.loc[df['Filename'] == 'mixed.txt', 'Numeric Data'].values[0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)