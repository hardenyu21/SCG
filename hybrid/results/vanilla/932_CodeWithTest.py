from collections import Counter
import re

def task_func(word: str) -> list:
    # Clean the word to include only alphabetic characters and convert to lowercase
    cleaned_word = re.sub(r'[^a-z]', '', word.lower())
    
    # If the cleaned word has fewer than 2 characters, return an empty list
    if len(cleaned_word) < 2:
        return []
    
    # Generate all two-letter combinations
    two_letter_combinations = [cleaned_word[i:i+2] for i in range(len(cleaned_word) - 1)]
    
    # Count the frequency of each two-letter combination
    combination_counts = Counter(two_letter_combinations)
    
    # Find the most common two-letter combination and its frequency
    most_common_combination, frequency = combination_counts.most_common(1)[0]
    
    # Return the result as a list containing a single tuple
    return [(most_common_combination, frequency)]
import unittest
class TestCases(unittest.TestCase):
    def test_repeating_pairs(self):
        self.assertEqual(task_func("aabbcc"), [('aa', 1)], "Should identify single repeating pair")
        
    def test_mixed_repeating_pairs(self):
        self.assertEqual(task_func("abcabc"), [('ab', 2)], "Should identify most frequent pair in mixed sequence")
        
    def test_single_character(self):
        self.assertEqual(task_func("a"), [], "Should return empty list for single character")
        
    def test_unique_pairs(self):
        self.assertEqual(task_func("abcdef"), [('ab', 1)], "Should handle all unique pairs")
        
    def test_empty_string(self):
        self.assertEqual(task_func(""), [], "Should return empty list for empty string")
    def test_case_insensitive(self):
        # Corrected the expected count to match the correct behavior of the function
        self.assertEqual(task_func("aAaAbbBB"), [('aa', 3)], "Should be case-insensitive")
    def test_ignore_non_alphabetic(self):
        self.assertEqual(task_func("abc123abc!"), [('ab', 2)], "Should ignore non-alphabetic characters")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)