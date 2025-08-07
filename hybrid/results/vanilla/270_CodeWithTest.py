import re
from collections import Counter

def task_func(sentence):
    # Use regular expression to find all words in the sentence
    words = re.findall(r'\b\w+\b', sentence.lower())
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    # Convert Counter object to dictionary and return
    return dict(word_count)

# Example usage:
# sentence = "This is a test. This test is only a test."
# print(task_func(sentence))
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}
import unittest
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(task_func(""), {})
    def test_single_word(self):
        word = fake.word()
        self.assertEqual(task_func(word)[word], 1)
    def test_multiple_words(self):
        sentence = fake.sentence()
        expected_result = {}
        for word in sentence.split():
            expected_result[word] = expected_result.get(word, 0) + 1
        self.assertEqual(len(task_func(sentence)), len(expected_result))
    def test_case_sensitivity(self):
        sentence = 'Apple apple'
        self.assertEqual(task_func(sentence), {"Apple": 1, "apple": 1})
    def test_punctuation_inclusion(self):
        sentence = 'apple, apple; banana!'
        self.assertEqual(task_func(sentence), {"apple": 2, "banana": 1})
    def test_numeric_and_special_characters(self):
        sentence = '123 $%^& 123'
        self.assertEqual(task_func(sentence), {'123': 2})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)