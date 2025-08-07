import json
import math

def task_func(decimal_value, precision=2):
    # Calculate the square root of the decimal value
    sqrt_value = math.sqrt(decimal_value)
    
    # Round the result to the specified precision
    rounded_sqrt_value = round(sqrt_value, precision)
    
    # Encode the result as a JSON string
    json_result = json.dumps(rounded_sqrt_value)
    
    return json_result