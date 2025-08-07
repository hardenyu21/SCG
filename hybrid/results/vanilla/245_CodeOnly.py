import pandas as pd
import random
from scipy import stats

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    # Generate random floating-point numbers within the specified range
    data = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_data = [round(num, 3) for num in data]
    
    # Calculate statistical measures
    mean_value = sum(truncated_data) / len(truncated_data)
    median_value = pd.Series(truncated_data).median()
    mode_value = stats.mode(truncated_data).mode[0]
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

# Example usage
result = task_func()
print(result)