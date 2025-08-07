import inspect
import types

def task_func(f):
    # Check if the function is a lambda
    is_lambda = isinstance(f, types.LambdaType)
    
    # Get the function's name
    func_name = f.__name__
    
    # Get the full argument specification
    sig = inspect.signature(f)
    
    # Extract arguments, defaults, and annotations
    args = []
    defaults = {}
    annotations = {}
    
    for param_name, param in sig.parameters.items():
        args.append(param_name)
        if param.default is not param.empty:
            defaults[param_name] = param.default
        if param.annotation is not param.empty:
            annotations[param_name] = param.annotation
    
    # Add return annotation if present
    if sig.return_annotation is not inspect.Signature.empty:
        annotations['return'] = sig.return_annotation
    
    # Construct the result dictionary
    result = {
        'name': func_name,
        'is_lambda': is_lambda,
        'arguments': args,
        'defaults': defaults,
        'annotations': annotations
    }
    
    return result
import unittest
class TestCases(unittest.TestCase):
    def test_regular_function(self):
        def test_func(a, b=1): pass
        result = task_func(test_func)
        self.assertEqual(result['function_name'], 'test_func')
        self.assertListEqual(result['args'], ['a', 'b'])
        self.assertTupleEqual(result['defaults'], (1,))
    def test_lambda_function(self):
        lambda_func = lambda x, y=2: x + y
        result = task_func(lambda_func)
        self.assertTrue(result['is_lambda'])
    def test_no_arguments(self):
        def test_func(): pass
        result = task_func(test_func)
        self.assertEqual(len(result['args']), 0)
    def test_annotations(self):
        def test_func(a: int, b: str = 'hello') -> int: pass
        result = task_func(test_func)
        self.assertIn('a', result['annotations'])
        self.assertIn('return', result['annotations'])
    def test_defaults_none(self):
        def test_func(a, b=None): pass
        result = task_func(test_func)
        self.assertIsNone(result['defaults'][0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)