import json
import math

def task_func(decimal_value, precision=2):
    # Calculate the square root of the decimal value
    sqrt_value = math.sqrt(decimal_value)
    
    # Round the result to the specified precision
    rounded_sqrt_value = round(sqrt_value, precision)
    
    # Encode the result as a JSON string
    json_result = json.dumps(rounded_sqrt_value)
    
    return json_result
import unittest
import doctest
from decimal import Decimal
class TestCases(unittest.TestCase):
    def test_case_1(self):
        decimal_value = Decimal('4.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "2.0")
    def test_case_2(self):
        decimal_value = Decimal('0.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "0.0")
    def test_case_3(self):
        decimal_value = Decimal('0.0001')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "0.01")
    def test_case_4(self):
        decimal_value = Decimal('1000000.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "1000.0")
    def test_case_5(self):
        decimal_value = Decimal('-1.0')
        with self.assertRaises(ValueError):
            task_func(decimal_value)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)