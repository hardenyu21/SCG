import string
import random
import re

def task_func(elements, pattern, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # List to store formatted elements
    formatted_elements = []
    
    # Iterate over each element in the elements list
    for element in elements:
        # Replace each character in the element with a random character
        replaced_element = ''.join(random.choice(string.ascii_letters) for _ in element)
        
        # Format the replaced element into the pattern "%{0}%"
        formatted_element = f"%{replaced_element}%"
        
        # Append the formatted element to the list
        formatted_elements.append(formatted_element)
    
    # Concatenate all formatted elements into a single string
    concatenated_string = ''.join(formatted_elements)
    
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_string) is not None
    
    # Return the list of formatted elements and the search result
    return formatted_elements, search_result
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Basic test with a given list of elements
        elements = ["abc", "def"]
        replaced_elements, res = task_func(elements, ".*", 234)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertTrue(res)
    def test_case_2(self):
        # Test with a single-character list of elements
        elements = ["a"]
        # Test with a complex pattern
        pattern = ".*[a-z]{3}.*"
        replaced_elements, res = task_func(elements, pattern, 104)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertFalse(res)
    def test_case_3(self):
        # Test with a longer list of elements
        elements = ["abcdefgh", "ijklmnop", "qrstuvwxyz"]
        replaced_elements, res = task_func(elements, "%+", 101)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertTrue(res)
    def test_case_4(self):
        # Test with an empty list of elements
        elements = []
        replaced_elements, _ = task_func(elements, ".*", 123)
        self.assertEqual(len(replaced_elements), len(elements))
    def test_case_5(self):
        # Test with a list containing mixed-case elements
        elements = ["AbC", "dEfG", "HijKL"]
        replaced_elements, _ = task_func(elements, ".*", 456)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)