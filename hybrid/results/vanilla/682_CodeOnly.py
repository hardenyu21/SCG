from collections import Counter
import math

def task_func(nested_dict):
    # Initialize a Counter to aggregate values
    aggregated_values = Counter()
    
    # Iterate over each key-value pair in the nested dictionary
    for key, value in nested_dict.items():
        # Check if the value is a dictionary
        if isinstance(value, dict):
            # Iterate over each sub-key-value pair in the nested dictionary
            for sub_key, sub_value in value.items():
                # If the sub_key is not "ele", add the sub_value to the Counter
                if sub_key != "ele":
                    aggregated_values[key] += sub_value
    
    # Create a new dictionary to store the sine of the aggregated values
    result = {}
    for key, total_value in aggregated_values.items():
        # Calculate the sine of the aggregated value
        result[key] = math.sin(total_value)
    
    return result