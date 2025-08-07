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