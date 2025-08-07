import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    # Create a dictionary with random lists of integers
    random_dict = {letter: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for letter in LETTERS}
    
    # Function to calculate population standard deviation
    def population_std_dev(numbers):
        if len(numbers) == 0:
            return 0
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)
    
    # Calculate the population standard deviation for each list
    std_dev_dict = {letter: population_std_dev(numbers) for letter, numbers in random_dict.items()}
    
    return std_dev_dict

# Example usage
# result = task_func(['a', 'b', 'c'])
# print(result)