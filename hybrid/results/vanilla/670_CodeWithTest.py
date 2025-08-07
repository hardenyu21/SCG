def task_func(x, w):
    max_weight = float('-inf')
    max_substr = ""
    
    # Iterate over all possible starting points of substrings
    for start in range(len(x)):
        current_weight = 0
        current_substr = ""
        
        # Iterate over all possible ending points of substrings starting from 'start'
        for end in range(start, len(x)):
            current_char = x[end]
            current_weight += w.get(current_char, 0)
            current_substr += current_char
            
            # Update max_weight and max_substr if the current substring has a higher weight
            if current_weight > max_weight:
                max_weight = current_weight
                max_substr = current_substr
    
    return max_substr

# Example usage:
x = "abcde"
w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(task_func(x, w))  # Output: "abcde"
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(task_func('c', {'a': 1, 'b': 2, 'c': 3}), 'c')
    
    def test_case_2(self):
        self.assertEqual(task_func('aabc', {'a': 10, 'b': -5, 'c': 3}), 'aa')
    def test_case_3(self):
        self.assertEqual(task_func('aabc', {'a': 10, 'b': -2, 'c': 3}), 'aabc')
    def test_case_4(self):
        self.assertEqual(task_func('aabc', {'a': 2, 'b': -5, 'c': 3}), 'aa')
    
    def test_case_5(self):
        self.assertEqual(task_func('aabc', {'a': 0, 'b': -1, 'c': 1}), 'c')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)