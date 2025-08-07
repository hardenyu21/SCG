import inspect
import types
import json

def task_func(f):
    # Check if the function is a lambda
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    func_name = f.__name__
    
    # Get the function's signature
    sig = inspect.signature(f)
    
    # Extract arguments and their default values
    args = []
    for param_name, param in sig.parameters.items():
        arg_info = {
            "name": param_name,
            "default": param.default if param.default is not param.empty else None,
            "annotation": str(param.annotation) if param.annotation is not param.empty else None
        }
        args.append(arg_info)
    
    # Get the function's annotations
    annotations = {k: str(v) for k, v in f.__annotations__.items()}
    
    # Create the specifications dictionary
    specifications = {
        "name": func_name,
        "arguments": args,
        "is_lambda": is_lambda,
        "annotations": annotations
    }
    
    # Convert the specifications dictionary to a JSON string
    return json.dumps(specifications, indent=4)

# Example usage:
# def example_func(a: int, b: str = "default") -> bool:
#     return True

# print(task_func(example_func))
import unittest
import json
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def sample_function(x, y, z=3): pass
        result = json.loads(task_func(sample_function))
        self.assertEqual(result['function_name'], 'sample_function')
        self.assertIn('y', result['args'])
    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = json.loads(task_func(lambda_func))
        self.assertTrue(result['is_lambda'])
        self.assertEqual(result['function_name'], '<lambda>')
    def test_no_arguments(self):
        def no_arg_func(): pass
        result = json.loads(task_func(no_arg_func))
        self.assertEqual(len(result['args']), 0)
    def test_function_with_no_defaults(self):
        def func_no_defaults(x, y): pass
        result = json.loads(task_func(func_no_defaults))
        self.assertIsNone(result['defaults'])
    def test_function_name(self):
        def simple_function(): pass
        result = json.loads(task_func(simple_function))
        self.assertEqual(result['function_name'], 'simple_function')
    
    def test_function_annotations(self):
        def annotated_function(x: int, y: str = 'hello') -> None: pass
        result = json.loads(task_func(annotated_function))
        self.assertDictEqual(result['annotations'], {'x': 'int', 'y': 'str', 'return': 'None'})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)