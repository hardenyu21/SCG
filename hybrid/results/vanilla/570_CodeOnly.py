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