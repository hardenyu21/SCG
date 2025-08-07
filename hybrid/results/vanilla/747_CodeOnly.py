import re
import math

def task_func(s):
    # Use regular expression to find all numbers in the string
    numbers = re.findall(r'-?\d+\.?\d*', s)
    
    # Initialize count and sqrt_sum
    count = 0
    sqrt_sum = 0.0
    
    # Iterate over the found numbers
    for num_str in numbers:
        # Convert the string to a float
        num = float(num_str)
        
        # Increment the count
        count += 1
        
        # Add the square root of the number to the sum
        sqrt_sum += math.sqrt(abs(num))  # Use abs to handle negative numbers
    
    return count, sqrt_sum

# Example usage:
# s = "3, 4.5, -2, 7, 0.25"
# count, sqrt_sum = task_func(s)
# print(f"Count: {count}, Sum of square roots: {sqrt_sum}")