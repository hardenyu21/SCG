import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    # Check if the input string is a string
    if not isinstance(string, str):
        raise TypeError("The input string must be a str.")
    
    # Check if patterns is a list of strings
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("Patterns must be a list of str.")
    
    # Initialize a dictionary to store the counts of each pattern
    pattern_counts = collections.defaultdict(int)
    
    # Iterate over each pattern and count its occurrences in the string
    for pattern in patterns:
        # Use re.findall to find all non-overlapping occurrences of the pattern
        matches = re.findall(pattern, string)
        # Update the count for the current pattern
        pattern_counts[pattern] = len(matches)
    
    # Convert defaultdict to a regular dict before returning
    return dict(pattern_counts)
import unittest
class TestCases(unittest.TestCase):
    def test_empty_pattern(self):
        'empty pattern'
        result = task_func('asdf', patterns=[])
        expected_result = {}
        self.assertEqual(result, expected_result)
    
    def test_wrong_type(self):
        'wrong input types'
        self.assertRaises(Exception, task_func, {'string': 123})
        self.assertRaises(Exception, task_func, {'string': ['asdf']})
        self.assertRaises(Exception, task_func, {'string': {'a': 3}})
        self.assertRaises(Exception, task_func, {'string': ['test'], 'patterns': 3})
        self.assertRaises(Exception, task_func, {'string': ['test'], 'patterns': ['3', 1]})
    def test_case_1(self):
        result = task_func("nnnaaaasssdddeeefffggg")
        expected_result = {'nnn': 1, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        result = task_func("")
        expected_result = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
        self.assertEqual(result, expected_result)
    
    def test_case_3(self):
        result = task_func("xyz")
        expected_result = {'nnn': 0, 'aaa': 0, 'sss': 0, 'ddd': 0, 'fff': 0}
        self.assertEqual(result, expected_result)
    
    def test_case_4(self):
        result = task_func("nnnaaannnsssdddfffnnn")
        expected_result = {'nnn': 3, 'aaa': 1, 'sss': 1, 'ddd': 1, 'fff': 1}
        self.assertEqual(result, expected_result)
    
    def test_case_5(self):
        result = task_func("xxxyyyzzz", patterns=['xxx', 'yyy', 'zzz', 'aaa'])
        expected_result = {'xxx': 1, 'yyy': 1, 'zzz': 1, 'aaa': 0}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)