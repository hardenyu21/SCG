from collections import deque
import math

def task_func(l):
    # Create a deque from the input list
    dq = deque(l)
    
    # Rotate the deque to the right by 3 positions
    dq.rotate(3)
    
    # Calculate the sum of numeric elements in the deque
    numeric_sum = sum(x for x in dq if isinstance(x, (int, float)))
    
    # Calculate the square root of the sum if there are any numeric elements
    if numeric_sum > 0:
        sqrt_sum = math.sqrt(numeric_sum)
        print(f"The square root of the sum of numeric elements: {sqrt_sum}")
    
    # Return the deque
    return dq

# Example usage
result = task_func([1, 2, 3, 4, 5])
print(result)