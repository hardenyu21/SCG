import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract "from_user" values
    from_user_values = result.get('from_user', [])
    
    # Check if the list is empty
    if not from_user_values:
        # Return a Series with NaN values for all statistics
        return pd.Series({
            'mean': np.nan,
            'median': np.nan,
            'min': np.nan,
            'max': np.nan,
            'std': np.nan,
            'current_time': datetime.now().strftime(DATE_FORMAT)
        })
    
    # Convert to numpy array
    from_user_array = np.array(from_user_values)
    
    # Check if all values are numeric
    if not np.issubdtype(from_user_array.dtype, np.number):
        raise ValueError("The 'from_user' values are not numeric.")
    
    # Calculate statistics
    mean_value = np.mean(from_user_array)
    median_value = np.median(from_user_array)
    min_value = np.min(from_user_array)
    max_value = np.max(from_user_array)
    std_value = np.std(from_user_array)
    
    # Get current date and time
    current_time = datetime.now().strftime(DATE_FORMAT)
    
    # Create a pandas Series with the results
    summary = pd.Series({
        'mean': mean_value,
        'median': median_value,
        'min': min_value,
        'max': max_value,
        'std': std_value,
        'current_time': current_time
    })
    
    return summary