from collections import Counter
import json
import random

# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def task_func(n, file_name, seed=77):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Randomly select n words from the WORDS list
    selected_words = random.sample(WORDS, min(n, len(WORDS)))
    
    # Count the occurrences of each word
    word_count = Counter(selected_words)
    
    # Write the word count to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(word_count, json_file, indent=4)
    
    # Return the name of the generated JSON file
    return file_name

# Example usage:
# file_name = task_func(5, 'word_count.json')
# print(f"JSON file generated: {file_name}")
import unittest
import os
import doctest
class TestCases(unittest.TestCase):
    file_name = "word_counts.json"
    def tearDown(self) -> None:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
    def test_case_1(self):
        # Test with n = 3
        self.file_name = task_func(3, self.file_name)
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 3)
        
    def test_case_2(self):
        # Test with n = 5
        self.file_name = task_func(5, self.file_name, 29)
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 5)
        # Test if the counts are correct
        self.assertEqual(data['honeydew'], 1)
        self.assertEqual(data['elderberry'], 1)
        self.assertEqual(data['grape'], 1)
        self.assertEqual(data['cherry'], 1)
        self.assertEqual(data['banana'], 1)
        
    def test_case_3(self):
        # Test with n less than 1
        with self.assertRaises(ValueError):
            task_func(0, self.file_name)
            
    def test_case_4(self):
        # Test with n greater than length of WORDS list
        with self.assertRaises(ValueError):
            task_func(100, self.file_name)
            
    def test_case_5(self):
        # Test with n equal to length of WORDS list
        self.file_name = task_func(
            len(
                ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
            ),
            self.file_name
        )
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(
            len(data), 
            len(
                ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
            )
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)