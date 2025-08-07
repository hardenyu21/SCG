from nltk.tokenize import RegexpTokenizer
from string import punctuation
import os

def task_func(text, output_filename):
    # Tokenizer to extract words starting with '$'
    tokenizer = RegexpTokenizer(r'\$\w+')
    # Extract words starting with '$'
    words = tokenizer.tokenize(text)
    
    # Filter out words that are solely composed of punctuation characters
    filtered_words = [word for word in words if any(char not in punctuation for char in word[1:])]
    
    # Get the absolute path of the output file
    output_path = os.path.abspath(output_filename)
    
    # Write the filtered words to the output file
    with open(output_path, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')
    
    # Return the absolute path to the output file
    return output_path
import unittest
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.filenames = []
        for i in range(1,7):
            self.filenames.append("task_func_test_output_"+str(i)+".txt")
    def tearDown(self):
        # Clean up the test file
        for filename in self.filenames:
            if os.path.exists(filename):
                os.remove(filename)
        
    def test_case_1(self):
        # Input 1
        text = "$abc def $efg $hij klm $ $abc $abc $hij $hij"
        filename = self.filenames[0]
        expected_words = ["$abc", "$efg", "$hij", "$abc", "$abc", "$hij", "$hij"]
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
    def test_case_2(self):
        # Input 2
        text = "There are no dollar words here."
        filename = self.filenames[1]
        expected_words = []
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
    def test_case_3(self):
        # Input 3
        text = "$$$$ $$ $$$$ $abc$ $def"
        filename = self.filenames[2]
        expected_words = ["$abc", "$def"]
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
    def test_case_4(self):
        # Input 4
        text = "$hello $world! This is a $test."
        filename = self.filenames[3]
        expected_words = ["$hello", "$world", "$test"]
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
    def test_case_5(self):
        # Input 5
        text = "$"
        filename = self.filenames[4]
        expected_words = []
        output_path = task_func(text, filename)
        with open(output_path, 'r') as file:
            saved_words = file.read().splitlines()
        self.assertEqual(saved_words, expected_words)
        self.assertTrue(os.path.exists(output_path))
    def test_save_dollar_prefixed_words_to_file(self):
        # Example input text containing various cases
        input_text = "$example $valid word $!invalid $$ $1234"
        # Temporary output file name for testing
        filename = self.filenames[5]
        # Expected result: Only valid $ prefixed words should be saved
        expected_words = ["$example", "$valid", "$1234"]
        expected_output = "\n".join(expected_words) + "\n"
        # Call the function with the test data
        output_path = task_func(input_text, filename)
        # Verify the file was created
        self.assertTrue(os.path.exists(output_path))
        # Open the file and read its contents
        with open(filename, 'r') as file:
            content = file.read()
        # Check the content against the expected output
        self.assertEqual(content, expected_output)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)