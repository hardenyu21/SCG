import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length from the predefined list of letters
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))
    
    # Count the frequency of each letter in the generated string
    frequency_counter = collections.Counter(random_string)
    
    # Sort the frequency counter by frequency in descending order
    sorted_frequency = sorted(frequency_counter.items(), key=lambda item: item[1], reverse=True)
    
    # Create an ordered dictionary from the sorted frequency list
    ordered_frequency_dict = collections.OrderedDict(sorted_frequency)
    
    return ordered_frequency_dict

# Example usage
if __name__ == "__main__":
    result = task_func(100)
    print(result)
import unittest
import collections
class TestCases(unittest.TestCase):
    def test_default_length(self):
        random.seed(0)
        freq = task_func()
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 100, "Total count of letters should be 100 for default length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_specific_length(self):
        random.seed(0)
        freq = task_func(50)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 50, "Total count of letters should be 50 for specific length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_minimum_length(self):
        random.seed(0)
        freq = task_func(1)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 1, "Total count of letters should be 1 for minimum length")
        self.assertEqual(len(freq), 1, "Only one letter should be present for minimum length")
    def test_large_length(self):
        random.seed(0)
        freq = task_func(1000)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 1000, "Total count of letters should be 1000 for large length")
        self.assertTrue(all(freq[key] >= freq[key2] for key, key2 in zip(list(freq)[:-1], list(freq)[1:])), "Frequencies should be sorted in descending order")
    def test_zero_length(self):
        random.seed(0)
        freq = task_func(0)
        self.assertIsInstance(freq, collections.OrderedDict, "Output should be an OrderedDict")
        self.assertEqual(sum(freq.values()), 0, "Total count of letters should be 0 for zero length")
        self.assertEqual(len(freq), 0, "No letters should be present for zero length")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)