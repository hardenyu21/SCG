import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    # Function to count words in a string
    def count_words(text):
        # Use regex to find words
        words = re.findall(r'\b\w+\b', text)
        return len(words)
    
    # Count words in both texts
    words1 = count_words(text1)
    words2 = count_words(text2)
    
    # Check if the number of words is the same
    if words1 != words2:
        return np.nan, np.nan
    
    # Convert the number of words to arrays (for t-test)
    data1 = np.array([words1])
    data2 = np.array([words2])
    
    # Perform paired t-test
    t_statistic, p_value = ttest_rel(data1, data2)
    
    return t_statistic, p_value
import unittest
import re
import numpy as np
from scipy.stats import ttest_rel
class TestCases(unittest.TestCase):
    def test_1(self):
        t_stat, p_val = task_func("Hello, world!", "Hi, universe!")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
    def test_2(self):
        t_stat, p_val = task_func("Short text.", "This is a slightly longer text.")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
    def test_3(self):
        t_stat, p_val = task_func("A, B, C, D, E.", "F, G, H, I, J.")
        self.assertTrue(isinstance(t_stat, float))
        self.assertTrue(isinstance(p_val, float))
        
    def test_4(self):
        t_stat, p_val = task_func("", "")
        self.assertTrue(np.isnan(t_stat))
        self.assertTrue(np.isnan(p_val))
    def test_5(self):
        t_stat, p_val = task_func("Testing with similar lengths.", "Testing with similar lengths.")
        self.assertTrue(np.isnan(t_stat))  # Since the lengths are the same, t-statistic should be NaN
        self.assertTrue(np.isnan(p_val))
    def test_unequal_lengths(self):
        t_stat, p_val = task_func("Short text.", "This is a slightly longer text.")
        self.assertTrue(np.isnan(t_stat))
        self.assertTrue(np.isnan(p_val))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)