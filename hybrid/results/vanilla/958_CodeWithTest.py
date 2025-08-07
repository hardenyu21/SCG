import random
import re

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    
    def scramble_word(word):
        if len(word) <= 3:
            return word
        # Extract the first and last letters
        first, last = word[0], word[-1]
        # Scramble the middle part
        middle = list(word[1:-1])
        random.shuffle(middle)
        # Reconstruct the word
        return first + ''.join(middle) + last
    
    # Use regex to find words and apply scrambling
    scrambled_text = re.sub(r'\b\w+\b', lambda match: scramble_word(match.group()), text)
    
    return scrambled_text
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a simple sentence
        input_text = "Hello world"
        output_text = task_func(input_text, seed=1)
        self.assertTrue(output_text.startswith("H"))
        self.assertTrue(output_text.endswith("d"))
        self.assertEqual(len(input_text.split()), len(output_text.split()))
    def test_case_2(self):
        # Test with single word
        input_text = "Programming"
        output_text = task_func(input_text, seed=2)
        self.assertTrue(output_text.startswith("P"))
        self.assertTrue(output_text.endswith("g"))
        self.assertEqual(len(input_text), len(output_text))
    def test_case_3(self):
        # Test with a sentence having punctuation
        input_text = "Hello, world!"
        output_text = task_func(input_text, seed=3)
        self.assertTrue(output_text.startswith("H"))
        self.assertTrue(output_text.endswith("!"))
        self.assertEqual(len(input_text.split()), len(output_text.split()))
    def test_case_4(self):
        # Test with a sentence having numbers
        input_text = "I have 2 cats"
        output_text = task_func(input_text, seed=4)
        self.assertTrue(output_text.startswith("I"))
        self.assertTrue(output_text.endswith("s"))
        self.assertTrue("2" in output_text)
        self.assertEqual(len(input_text.split()), len(output_text.split()))
    def test_case_5(self):
        # Test with empty string
        input_text = ""
        output_text = task_func(input_text, seed=5)
        self.assertEqual(output_text, "")
    def test_case_6(self):
        # Test with words containing digits and special characters
        input_text = "Python3 is fun!"
        output_text = task_func(input_text, seed=6)
        self.assertTrue(output_text.startswith("P") and output_text.endswith("!"))
        self.assertIn("3", output_text)
    def test_case_7(self):
        # Test words that are 3 characters long
        input_text = "Can you see the cat?"
        output_text = task_func(input_text, seed=8)
        self.assertIn("Can", output_text)
        self.assertIn("the", output_text)
        self.assertIn("cat", output_text)
    def test_case_8(self):
        # Test with a longer paragraph
        input_text = (
            "This is a longer text to see how the function handles more complex inputs."
        )
        output_text = task_func(input_text, seed=9)
        self.assertGreaterEqual(
            len(output_text.split()), 10
        )  # Ensure it's a long input
    def test_case_9(self):
        # Test with non-English characters
        input_text = "Привет, как дела?"
        output_text = task_func(input_text, seed=10)
        self.assertTrue(output_text.startswith("П") and output_text.endswith("?"))
    def test_case_10(self):
        # Test reproducibility with the same seed
        input_text = "Reproducibility test"
        output_text1 = task_func(input_text, seed=11)
        output_text2 = task_func(input_text, seed=11)
        self.assertEqual(output_text1, output_text2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)