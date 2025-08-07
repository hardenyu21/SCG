import re
import os
import glob

def task_func(directory, word):
    count = 0
    # Use glob to find all files in the directory
    for file_path in glob.glob(os.path.join(directory, '*')):
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            try:
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # Use regular expression to find the word
                    if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
                        count += 1
            except Exception as e:
                # Handle any exceptions that occur while reading the file
                print(f"Error reading {file_path}: {e}")
    return count
import unittest
from pyfakefs.fake_filesystem_unittest import TestCase
class TestCases(TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        self.directory = '/mnt/data/documents'
        self.fs.create_dir(self.directory)
        self.fs.create_file('/mnt/data/documents/apple.txt', contents='Apple is great.')
        self.fs.create_file('/mnt/data/documents/word.txt', contents='This file contains the word. Word is important. Word up!')
        self.fs.create_file('/mnt/data/documents/banana.txt', contents='Banana is yellow.')
        self.fs.create_file('/mnt/data/documents/orange.txt', contents='Orange is sweet.')
        self.fs.create_file('/mnt/data/documents/grape.txt', contents='I like grapes. Grapes are nice.')
    def test_1(self):
        result = task_func(self.directory, 'apple')
        self.assertEqual(result, 1) 
    def test_2(self):
        result = task_func(self.directory, 'word')
        self.assertEqual(result, 1)  # Ensuring 3 files contain the word "word" 
    def test_3(self):
        result = task_func(self.directory, 'banana')
        self.assertEqual(result, 1)  # Should be 1 file that contains "banana" multiple times
    def test_4(self):
        result = task_func(self.directory, 'orange')
        self.assertEqual(result, 1)  # 1 file contains the word "orange"
    def test_5(self):
        result = task_func(self.directory, 'grapes')
        self.assertEqual(result, 1)  # Ensuring 1 file contains the word "grape"


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)