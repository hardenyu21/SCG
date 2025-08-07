from functools import reduce
import operator
import string

def task_func(letters):
    # Create a dictionary mapping each uppercase letter to its corresponding number
    letter_to_number = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=1)}
    
    # Map the input letters to their corresponding numbers using the dictionary
    numbers = [letter_to_number[letter] for letter in letters]
    
    # Calculate the product of the numbers using reduce and operator.mul
    product = reduce(operator.mul, numbers, 1)
    
    return product

# Example usage
print(task_func(["A", "E", "I"]))  # Output: 45