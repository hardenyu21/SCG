import pandas as pd
import re
from scipy import stats
import matplotlib.pyplot as plt

def task_func(text):
    # Extract names not surrounded by square brackets
    names = re.findall(r'\b(?!\[)[A-Za-z]+\b(?!\])', text)
    
    # Count the frequency of each name
    name_counts = pd.Series(names).value_counts()
    
    # Create a bar chart of the name frequencies
    ax = None
    if not name_counts.empty:
        ax = name_counts.plot(kind='bar', title='Name Frequencies')
        plt.xlabel('Name')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
    
    # Calculate skewness and kurtosis
    skewness = stats.skew(name_counts) if not name_counts.empty else None
    kurtosis = stats.kurtosis(name_counts) if not name_counts.empty else None
    
    return name_counts, ax, skewness, kurtosis
import unittest
import doctest
test_data = [
    # Test Case 1: Basic names separated by addresses in square brackets
    "John Doe [123 MAIN ST, TOWN, ST 12345]Jane Smith [456 OTHER ST, CITY, ST 67890]",
    
    # Test Case 2: Multiple occurrences of the same name
    "Alice [111 ALPHA ST, PLACE, ST 11111]Bob [222 BETA ST, LOCATION, ST 22222]Alice [333 GAMMA ST, REGION, ST 33333]",
    
    # Test Case 3: Names with special characters and different patterns
    "Mr. X [444 X ST, XPLACE, ST 44444]Dr. Y [555 Y ST, YCITY, ST 55555]Z [666 Z ST, ZTOWN, ST 66666]",
    
    # Test Case 4: Empty string
    "",
    
    # Test Case 5: Only addresses without names
    "[777 FIRST ST, APLACE, ST 77777][888 SECOND ST, BCITY, ST 88888][999 THIRD ST, CTOWN, ST 99999]",
    # Long test case with multiple names and addresses
    "John Doe [123 MAIN ST, TOWN, ST 12345]Jane Smith [456 OTHER ST, CITY, ST 67890]Alice [111 ALPHA ST, PLACE, ST 11111]Bob [222 BETA ST, LOCATION, ST 22222]Alice [333 GAMMA ST, REGION, ST 33333]Mr. X [444 X ST, XPLACE, ST 44444]Dr. Y [555 Y ST, YCITY, ST 55555]Z [666 Z ST, ZTOWN, ST 66666]"
]
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test Case 1: Basic names separated by addresses in square brackets
        input_text = test_data[0]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["John Doe"], 1)
        self.assertEqual(name_freqs["Jane Smith"], 1)
        self.assertTrue("Name Frequencies" in plot.get_title())
    
    def test_case_2(self):
        # Test Case 2: Multiple occurrences of the same name
        input_text = test_data[1]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["Alice"], 2)
        self.assertEqual(name_freqs["Bob"], 1)
    
    def test_case_3(self):
        # Test Case 3: Names with special characters and different patterns
        input_text = test_data[2]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertEqual(name_freqs["Mr. X"], 1)
        self.assertEqual(name_freqs["Dr. Y"], 1)
        self.assertEqual(name_freqs["Z"], 1)
    
    def test_case_4(self):
        # Test Case 4: Empty string
        input_text = test_data[3]
        name_freqs, plot, _, _ = task_func(input_text)
        self.assertTrue(name_freqs.empty)
    
    def test_case_5(self):
        # Test Case 5: Only addresses without names
        input_text = test_data[4]
        name_freqs, plot, _, _ = task_func(input_text)
        print(name_freqs)
        self.assertTrue(name_freqs.empty)
        # Long test case with multiple names and addresses
        input_text = test_data[5]
        name_freqs, plot, skewness, kurtosis = task_func(input_text)
        self.assertEqual(name_freqs["John Doe"], 1)
        # Test for skewness and kurtosis
        self.assertAlmostEqual(skewness, 2.04, places=2)
        self.assertAlmostEqual(kurtosis, 2.17, places=2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)