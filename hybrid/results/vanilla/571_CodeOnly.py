import inspect
import pandas as pd
import os

def task_func(f_list, file_path):
    # Validate input
    if not isinstance(f_list, list) or not all(callable(f) for f in f_list):
        raise ValueError("f_list must be a list of functions.")
    if not f_list:
        raise ValueError("f_list is empty.")
    if not isinstance(file_path, str) or not os.path.isdir(os.path.dirname(file_path)):
        raise ValueError("file_path is not a valid path.")
    
    # Prepare data for CSV
    data = []
    for f in f_list:
        # Get function name
        func_name = f.__name__
        
        # Get number of arguments
        sig = inspect.signature(f)
        num_args = len(sig.parameters)
        
        # Get default values
        defaults = {k: v.default for k, v in sig.parameters.items() if v.default is not inspect.Parameter.empty}
        
        # Get annotations
        annotations = f.__annotations__
        
        # Check if the function is a lambda
        is_lambda = f.__name__ == "<lambda>"
        
        # Append data to list
        data.append({
            'Function Name': func_name,
            'Number of Arguments': num_args,
            'Defaults': defaults,
            'Annotations': annotations,
            'Is Lambda': is_lambda
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Write to CSV
    try:
        df.to_csv(file_path, index=False)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")
    
    return None