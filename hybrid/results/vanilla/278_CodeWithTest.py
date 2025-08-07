import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random coefficients a, b, and c between -10 and 10
    a = np.random.randint(-10, 11)
    b = np.random.randint(-10, 11)
    c = np.random.randint(-10, 11)
    
    # Ensure a is not zero to maintain the quadratic nature
    while a == 0:
        a = np.random.randint(-10, 11)
    
    # Define the variable and the quadratic equation
    x = symbols('x')
    equation = a * x**2 + b * x + c
    
    # Solve the quadratic equation
    solutions = solve(equation, x)
    
    # Round the solutions to the specified precision
    rounded_solutions = tuple(
        complex(round(sol.evalf().as_real_imag()[0], precision), 
                round(sol.evalf().as_real_imag()[1], precision))
        for sol in solutions
    )
    
    return rounded_solutions

# Example usage
print(task_func(precision=2, seed=0))
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = task_func(seed=1789)
        self.assertIsInstance(result, tuple, "The result should be a tuple.")
        self.assertEqual(len(result), 2, "The tuple should have two values.")
        for value in result:
            self.assertEqual(value.real, round(value.real, 2), "The value should be rounded to 2 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 2), "The value should be rounded to 2 decimal places.")
        # Test the output
        self.assertEqual(result, ((-5.15+0j), (0.41+0j)))
        
    def test_case_2(self):
        result = task_func(precision=3)
        for value in result:
            self.assertEqual(value.real, round(value.real, 3), "The value should be rounded to 3 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 3), "The value should be rounded to 3 decimal places.")
    def test_case_3(self):
        result = task_func(precision=0)
        for value in result:
            self.assertEqual(value.real, round(value.real), "The value should be an integer.")
            self.assertEqual(value.imag, round(value.imag), "The value should be an integer.")
    def test_case_4(self):
        result = task_func(precision=4)
        for value in result:
            self.assertEqual(value.real, round(value.real, 4), "The value should be rounded to 4 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 4), "The value should be rounded to 4 decimal places.")
    def test_case_5(self):
        result = task_func(precision=5, seed=1234)
        for value in result:
            self.assertEqual(value.real, round(value.real, 5), "The value should be rounded to 5 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 5), "The value should be rounded to 5 decimal places.")
        # Test the output
        self.assertEqual(result, ((0.19792-0.40336j), (0.19792+0.40336j)))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)