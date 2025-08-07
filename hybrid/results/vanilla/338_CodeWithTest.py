import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Function to generate a random alphanumeric string of length 5
    def generate_random_string():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    
    # Format each element in the list with the random pattern
    formatted_elements = [f"% {generate_random_string()}%" for _ in elements]
    
    # Count the occurrence of each character in all formatted strings
    char_count = {}
    for element in formatted_elements:
        for char in element:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Prepare data for the histogram
    characters = list(char_count.keys())
    counts = list(char_count.values())
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(characters, counts)
    ax.set_xlabel('Character')
    ax.set_ylabel('Count')
    ax.set_title('Character Occurrence in Formatted Strings')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Return the formatted elements, the plot axes, and the character count dictionary
    return formatted_elements, ax, char_count

# Example usage:
# elements = ["apple", "banana", "cherry"]
# formatted_elements, ax, char_count = task_func(elements)
# plt.show()
# print(formatted_elements)
# print(char_count)
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a list containing two strings
        result, ax, data = task_func(['hello', 'world'], seed=39)
        self.assertEqual(len(result), 2)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8) # 5 characters + 3 special characters
        
        # Test the histogram plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 12)
        # Test the character count dictionary
        self.assertEqual(data['%'], 4)
    def test_case_2(self):
        # Test with an empty list
        result, _, _ = task_func([])
        self.assertEqual(result, [])
    def test_case_3(self):
        # Test with a list containing multiple identical strings
        result, _, _ = task_func(['test', 'test', 'test'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)
    def test_case_4(self):
        # Test with a list containing single character strings
        result, ax, data = task_func(['a', 'b', 'c'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)
        # Test the character count dictionary
        self.assertEqual(data['C'], 2)
        self.assertEqual(data['%'], 6)
        self.assertEqual(data['V'], 1)
    
    def test_case_5(self):
        # Test with a list containing strings of varying lengths
        result, _, _ = task_func(['short', 'mediumlength', 'averyverylongstring'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)