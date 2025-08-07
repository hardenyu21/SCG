from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    # Validate input
    if not all(isinstance(n, int) and n >= 0 for n in numbers):
        raise ValueError("All elements in the input list must be non-negative integers.")
    
    # Use multiprocessing to calculate factorials in parallel
    with Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    
    # Convert list of tuples to dictionary
    return dict(results)

# Example usage:
# numbers = [0, 1, 2, 3, 4, 5]
# print(task_func(numbers))