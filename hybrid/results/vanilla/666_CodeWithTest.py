
import unittest
class TestCases(unittest.TestCase):
    def base(self, seq, letter_weight_dict, correct_seq):
        # Run function
        result = task_func(seq, letter_weight_dict)
        # Check result
        self.assertTrue(isinstance(result, str))
        self.assertEqual(result, correct_seq)
    def test_case_1(self):
        self.base('abc', {'a': 1, 'b': 2, 'c': 3}, 'abc')
    
    def test_case_2(self):
        self.base('aabc', {'a': 10, 'b': -5, 'c': 3}, 'aac')
    def test_case_3(self):
        self.base('zx', {'x': 1, 'z': 2}, 'zx')
    
    def test_case_4(self):
        self.base('lfhah', {'a': 1, 'f': 2, 'h': -1, 'l': 4}, 'lfa')
    
    def test_case_5(self):
        self.base('a', {'a': 1}, 'a')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)