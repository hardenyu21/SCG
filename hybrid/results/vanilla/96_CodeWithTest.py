import csv
from collections import Counter

def task_func(csv_file, csv_delimiter):
    word_counter = Counter()
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=csv_delimiter)
        
        for row in csv_reader:
            for cell in row:
                word_counter[cell] += 1
    
    # Sort the words by frequency in descending order
    sorted_word_count = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_word_count
import unittest
from unittest.mock import patch, mock_open
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """ Test that the function returns a list. """
        with patch('builtins.open', mock_open(read_data="word1,word2,word1")):
            result = task_func('dummy_path.csv', ',')
        self.assertIsInstance(result, list)
    def test_tuple_structure(self):
        """ Test that each element in the list is a tuple with two elements. """
        with patch('builtins.open', mock_open(read_data="word1,word2,word1")):
            result = task_func('dummy_path.csv', ',')
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
    def test_word_count(self):
        """ Test if the function correctly counts the occurrences of words. """
        with patch('builtins.open', mock_open(read_data="word1\nword2\nword1")):
            result = task_func('dummy_path.csv', ',')
        self.assertIn(('word1', 2), result)
        self.assertIn(('word2', 1), result)
    def test_empty_file(self):
        """ Test the function's behavior with an empty CSV file. """
        with patch('builtins.open', mock_open(read_data="")):
            result = task_func('dummy_path.csv', ',')
        self.assertEqual(len(result), 0)
    def test_no_repeated_words(self):
        """ Test the function's behavior with no repeated words. """
        with patch('builtins.open', mock_open(read_data="word1,word2,word3")):
            result = task_func('dummy_path.csv', ',')
        expected_counts = {('word1', 1), ('word2', 1), ('word3', 1)}
        self.assertTrue(all(pair in expected_counts for pair in result))
    def test_custom_delimiter(self):
        """ Test the function's behavior with a custom delimiter. """
        with patch('builtins.open', mock_open(read_data="word1;word2;word1")):
            result = task_func('dummy_path.csv', ';')
        self.assertIn(('word1', 2), result)
        self.assertIn(('word2', 1), result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)