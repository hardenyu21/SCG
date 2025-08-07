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