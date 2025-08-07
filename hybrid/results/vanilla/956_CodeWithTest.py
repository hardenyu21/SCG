import re
import string
import random

def task_func(text: str, seed=None) -> str:
    # Set the random seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Remove special characters (punctuation)
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    
    # Normalize whitespace
    text = text.replace(' ', '_')
    text = text.replace('\t', '__')
    text = text.replace('\n', '___')
    
    # Randomize character casing
    randomized_text = ''.join(
        char.upper() if random.random() < 0.5 else char.lower() for char in text
    )
    
    return randomized_text
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func("Hello   World!", seed=1)
        self.assertNotIn(" ", result, "Spaces should be replaced.")
        self.assertNotIn("!", result, "Special characters should be removed.")
        self.assertEqual(
            len(result), len("Hello___World"), "Length should match processed input."
        )
    def test_case_2(self):
        result = task_func("Python!", seed=2)
        self.assertNotIn("!", result, "Special characters should be removed.")
        self.assertEqual(
            len(result), len("Python"), "Length should match processed input."
        )
    def test_case_3(self):
        result = task_func("  ", seed=3)
        self.assertEqual(result, "__", "Spaces should be replaced with underscores.")
    def test_case_4(self):
        result = task_func("\t\n", seed=4)
        self.assertEqual(
            result, "_____", "Tab and newline should be replaced with underscores."
        )
    def test_case_5(self):
        result = task_func("a!b@c#", seed=5)
        self.assertTrue(result.isalpha(), "Output should only contain alphabets.")
        self.assertEqual(
            len(result), len("abc"), "Length should match processed input."
        )
    def test_case_6(self):
        # Test with all types of whitespace characters
        result = task_func("a b\tc\nd", seed=6)
        self.assertEqual(
            result.lower(),
            "a_b__c___d",
            "Should replace all types of whitespaces correctly.",
        )
    def test_case_7(self):
        # Test with a mix of alphanumeric and special characters
        result = task_func("a1! b2@ c3#", seed=7)
        self.assertTrue(
            all(char.isalnum() or char == "_" for char in result),
            "Should only contain alphanumeric characters and underscores.",
        )
    def test_case_8(self):
        # Test with an empty string
        result = task_func("", seed=8)
        self.assertEqual(result, "", "Should handle empty string correctly.")
    def test_case_9(self):
        # Test with a string that contains no special characters or whitespaces
        result = task_func("abcdefg", seed=9)
        self.assertTrue(result.isalpha(), "Should contain only letters.")
        self.assertEqual(len(result), 7, "Length should match the input.")
    def test_case_10(self):
        # Test with a long string of repeated characters
        result = task_func("a" * 50, seed=10)
        self.assertTrue(
            all(char.lower() == "a" for char in result),
            "All characters should be 'a' or 'A'.",
        )
        self.assertEqual(len(result), 50, "Length should match the input.")
    def test_case_11(self):
        # Test with only special characters
        result = task_func("!@#$%^&*", seed=11)
        self.assertEqual(
            result, "", "Should return an empty string for only special characters."
        )
    def test_case_12(self):
        # Test with numeric characters
        result = task_func("12345", seed=13)
        self.assertTrue(result.isdigit(), "Should contain only digits.")
        self.assertEqual(len(result), 5, "Length should match the input.")
    def test_case_13(self):
        # Test with a string containing only whitespace characters
        result = task_func(" \t\n", seed=14)
        self.assertEqual(
            result,
            "______",
            "Should replace all types of whitespaces correctly, with two underscores for tab and three for newline.",
        )
    def test_case_14(self):
        # Test the randomness of uppercase conversion with a long string
        result = task_func("a" * 100, seed=15)
        self.assertTrue(
            all(char.lower() == "a" for char in result),
            "All characters should be 'a' or 'A'.",
        )
        self.assertNotEqual(
            result, "a" * 100, "Should have some uppercase transformations."
        )
        self.assertNotEqual(
            result, "A" * 100, "Should have some lowercase transformations."
        )
    def test_case_15(self):
        # Test random seed impact
        result1 = task_func("test seed impact", seed=42)
        result2 = task_func("test seed impact", seed=42)
        self.assertEqual(
            result1, result2, "Results with the same seed should be identical."
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)