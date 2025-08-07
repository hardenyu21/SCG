import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(directory_path):
    unique_words = set()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()
                # Split the content into words
                words = content.split()
                # Filter out stopwords and add to the set of unique words
                unique_words.update(word.lower() for word in words if word.lower() not in STOPWORDS)
    
    # Return the count of unique non-stop words
    return len(unique_words)

# Example usage:
# print(task_func('/path/to/directory'))
import unittest
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_data'
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        for f in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, f))
        os.rmdir(self.test_dir)
    def test_no_text_files(self):
        self.assertEqual(task_func(self.test_dir), 0)
    def test_empty_text_files(self):
        with open(os.path.join(self.test_dir, 'empty.txt'), 'w') as f:
            pass
        self.assertEqual(task_func(self.test_dir), 0)
    def test_files_with_only_stopwords(self):
        with open(os.path.join(self.test_dir, 'stopwords.txt'), 'w') as f:
            f.write('the and or but')
        self.assertEqual(task_func(self.test_dir), 0)
    def test_non_empty_text_files(self):
        with open(os.path.join(self.test_dir, 'sample.txt'), 'w') as f:
            f.write('Hello world! This is a test.')
        self.assertEqual(task_func(self.test_dir), 3)  # 'Hello', 'world', 'This', 'test'
    def test_case_insensitivity(self):
        with open(os.path.join(self.test_dir, 'mixed_case.txt'), 'w') as f:
            f.write('Word word WoRd WORD')
        self.assertEqual(task_func(self.test_dir), 4)  # 'Word' in different cases


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)