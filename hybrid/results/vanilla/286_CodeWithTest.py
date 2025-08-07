from collections import Counter
import os
import csv

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    try:
        # Check if the directory exists
        if not os.path.isdir(test_directory):
            return 0

        # Initialize a Counter to keep track of word counts
        word_counter = Counter()

        # Iterate over all files in the directory
        for filename in os.listdir(test_directory):
            # Check if the file is a .txt file
            if filename.endswith('.txt'):
                file_path = os.path.join(test_directory, filename)
                # Open and read the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read all lines and split into words
                    words = file.read().split()
                    # Update the counter with words from this file
                    word_counter.update(words)

        # Write the word counts to a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header
            csv_writer.writerow(['Word', 'Count'])
            # Write the word counts
            for word, count in word_counter.items():
                csv_writer.writerow([word, count])

        # Return the total number of words
        return sum(word_counter.values())

    except Exception as e:
        # Return 0 if any error occurs
        return 0
import unittest
from unittest.mock import patch, MagicMock
from collections import Counter
from faker import Faker
import shutil
# Blackbox test cases
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_directory = './testdir_f270'
        os.makedirs(self.test_directory, exist_ok=True)
        
        self.output_file = 'test_output.csv'
        self.list_files = []
    # Function to create fake dictionary files
    def create_fake_dict_files(self, directory, num_files, num_words):
        fake = Faker()
        for _ in range(num_files):
            file_name = fake.file_name(extension='txt')
            self.list_files.append(os.path.join(directory, file_name))
            with open(os.path.join(directory, file_name), 'w') as file:
                words = [fake.word() for _ in range(num_words)]
                file.write(' '.join(words))
    
    #remove fake files
    def remove_files(self):
        for fn in self.list_files:
            if os.path.exists(fn):
               os.remove(fn)
        self.list_files = []
    def tearDown(self):
        # Remove the test_output.json file after each test
        if os.path.exists('test_output.csv'):
            os.remove('test_output.csv')
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
    def test_no_files_in_directory(self):
        # Test case where there are no txt files in the directory
        self.create_fake_dict_files(self.test_directory, 0, 0)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(result, 0)
        self.remove_files()
    
    def test_single_file_multiple_words(self):
        # Test case with a single file containing multiple words
        self.create_fake_dict_files(self.test_directory, 1, 50)
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(50,result)
        self.remove_files()
    def test_multiple_files_multiple_words(self):
        # Test case with multiple files each containing multiple words
        self.create_fake_dict_files(self.test_directory, 5, 20)
        result = task_func(self.output_file, self.test_directory)
        self.remove_files()
        self.assertEqual(100,result)
    def test_directory_does_not_exist(self):
        # Test case where the specified directory does not exist
        result = task_func(self.output_file, self.test_directory)
        self.assertEqual(0,result)
    def test_empty_files_in_directory(self):
        # Test case with empty txt files in the directory
        self.create_fake_dict_files(self.test_directory, 3, 0)
        result = task_func(self.output_file, self.test_directory)
        self.remove_files()
        self.assertEqual(0,result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)