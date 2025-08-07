import string
import matplotlib.pyplot as plt

def task_func(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    # Convert the string to lowercase to ensure case-insensitivity
    s = s.lower()
    
    # Initialize a dictionary to store the frequency of each letter
    frequency = {letter: 0 for letter in string.ascii_lowercase}
    
    # Calculate the frequency of each letter
    for char in s:
        if char in frequency:
            frequency[char] += 1
    
    # Filter out letters that do not appear in the string
    frequency = {letter: count for letter, count in frequency.items() if count > 0}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(frequency.keys(), frequency.values())
    ax.set_title('Letter Frequencies')
    ax.set_xlabel('Letters')
    ax.set_ylabel('Frequency')
    
    # Return the frequency dictionary and the Axes object
    return frequency, ax

# Example usage:
# freq, ax = task_func("Hello World!")
# plt.show()
import unittest
import string
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a simple sentence
        s = "This is a test string."
        expected_output = {
            letter: s.lower().count(letter) for letter in string.ascii_lowercase
        }
        result, ax = task_func(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_2(self):
        # Test with a string having all alphabets
        s = "abcdefghijklmnopqrstuvwxyz"
        expected_output = {letter: 1 for letter in string.ascii_lowercase}
        result, ax = task_func(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_3(self):
        # Test with a string having no alphabets
        s = "1234567890!@#$%^&*()"
        expected_output = {letter: 0 for letter in string.ascii_lowercase}
        result, ax = task_func(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_4(self):
        # Test with an empty string
        s = ""
        expected_output = {letter: 0 for letter in string.ascii_lowercase}
        result, ax = task_func(s)
        self.assertEqual(result, expected_output)
        self.assertEqual(ax.get_title(), "Letter Frequencies")
        self.assertEqual(ax.get_xlabel(), "Letters")
        self.assertEqual(ax.get_ylabel(), "Frequency")
    def test_case_5(self):
        # Test error handling
        for invalid in [123, []]:
            with self.assertRaises(Exception):
                task_func(invalid)
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)