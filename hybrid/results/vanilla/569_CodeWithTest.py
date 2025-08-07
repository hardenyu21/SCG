import inspect
import types
import math

def task_func(f):
    # Get the function's name
    func_name = f.__name__
    
    # Get the full argument specification of the function
    argspec = inspect.getfullargspec(f)
    
    # Calculate the number of arguments
    num_args = len(argspec.args) + len(argspec.kwonlyargs)
    
    # Calculate the square root of the number of arguments
    sqrt_num_args = math.sqrt(num_args)
    
    # Count the number of lambda functions in default values
    lambda_count = 0
    if argspec.defaults:
        for default in argspec.defaults:
            if isinstance(default, types.LambdaType):
                lambda_count += 1
    
    # Return the result as a dictionary
    return {
        'name': func_name,
        'sqrt_num_args': sqrt_num_args,
        'lambda_count': lambda_count
    }

# Example usage:
def example_function(a, b, c=lambda x: x, d=42):
    return a + b + c(d)

result = task_func(example_function)
print(result)
import unittest
import math
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def sample_function(x, y, z=3): pass
        result = task_func(sample_function)
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertEqual(result['sqrt_args'], math.sqrt(3))
    def test_lambda_in_defaults(self):
        def func_with_lambda(x, y=lambda a: a+2): pass
        result = task_func(func_with_lambda)
        self.assertEqual(result['lambda_in_defaults'], 1)
    def test_no_arguments(self):
        def no_arg_func(): pass
        result = task_func(no_arg_func)
        self.assertEqual(result['sqrt_args'], 0)
    def test_function_with_no_lambda_defaults(self):
        def func_without_lambda(x, y=2): pass
        result = task_func(func_without_lambda)
        self.assertEqual(result['lambda_in_defaults'], 0)
    def test_function_with_multiple_defaults(self):
        def sample_function(x, y=2, z=lambda a: a+2, w=lambda b: b*2): pass
        result = task_func(sample_function)
        self.assertEqual(result['lambda_in_defaults'], 2)
    def test_lambda_function(self):
        lambda_func = lambda x, y=lambda a: a * 2: x + y(2)
        result = task_func(lambda_func)
        self.assertEqual(result['function_name'], '<lambda>')
        self.assertEqual(result['sqrt_args'], math.sqrt(2), "Sqrt of args should be sqrt(2) for lambda_func with 2 args")
        self.assertEqual(result['lambda_in_defaults'], 1, "There should be 1 lambda in defaults")
    
    def test_sqrt_args_correctness(self):
        def test_func(a, b, c=3, d=lambda x: x + 1): pass
        result = task_func(test_func)
        self.assertEqual(result['sqrt_args'], math.sqrt(4), "Sqrt of args count should match expected value")
    # Test for edge case or error handling
    def test_non_function_input(self):
        with self.assertRaises(TypeError):
            task_func("This is not a function")
    # Directly verifying the math operation
    def test_math_operation_direct_check(self):
        def test_func(a, b, c=3, d=lambda x: x + 1): pass
        result = task_func(test_func)
        self.assertAlmostEqual(result['sqrt_args'], math.sqrt(4), msg="sqrt_args should accurately represent the square root of the number of arguments.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)