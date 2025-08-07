import re
import math

def task_func(s):
    # Use regular expression to find all numbers in the string
    numbers = re.findall(r'-?\d+\.?\d*', s)
    
    # Initialize count and sqrt_sum
    count = 0
    sqrt_sum = 0.0
    
    # Iterate over the found numbers
    for num_str in numbers:
        # Convert the string to a float
        num = float(num_str)
        
        # Increment the count
        count += 1
        
        # Add the square root of the number to the sum
        sqrt_sum += math.sqrt(abs(num))  # Use abs to handle negative numbers
    
    return count, sqrt_sum

# Example usage:
# s = "3, 4.5, -2, 7, 0.25"
# count, sqrt_sum = task_func(s)
# print(f"Count: {count}, Sum of square roots: {sqrt_sum}")
import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        count, sqrt_sum = task_func('1,2,3.5,abc,4,5.6')
        self.assertEqual(count, 5)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [1, 2, 3.5, 4, 5.6]))
    def test_2(self):
        count, sqrt_sum = task_func('a,b,c,10,20.5')
        self.assertEqual(count, 2)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [10, 20.5]))
    def test_3(self):
        count, sqrt_sum = task_func('1.1,2.2,3.3')
        self.assertEqual(count, 3)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [1.1, 2.2, 3.3]))
    def test_4(self):
        count, sqrt_sum = task_func('')
        self.assertEqual(count, 0)
        self.assertEqual(sqrt_sum, 0.0)
    def test_5(self):
        count, sqrt_sum = task_func('apple,banana,3.14,15,grape,1001')
        self.assertEqual(count, 3)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [3.14, 15, 1001]))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)