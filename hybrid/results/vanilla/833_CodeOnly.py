import random
from collections import Counter
from statistics import mode

def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate a random list of integers within the specified range
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    
    # Calculate the frequency of each number in the list
    frequency_counter = Counter(random_list)
    
    # Find the mode of the list
    list_mode = mode(random_list)
    
    # Create a generator that yields tuples of (number, frequency)
    def number_frequency_generator():
        for number, frequency in frequency_counter.items():
            yield (number, frequency)
    
    # Return the mode and the generator
    return list_mode, number_frequency_generator()

# Example usage
mode, numbers = task_func(20, -12, 334, random_seed=23)
print(mode)  # Output: 136
print([_ for _ in numbers])  # Output: [(136, 1), (30, 1), (-4, 1), (291, 1), (145, 1), (204, 1), (182, 1), (259, 1), (171, 1), (54, 1), (86, 1), (124, 1), (215, 1), (-5, 1), (101, 1), (305, 1), (220, 1), (0, 1), (42, 1), (31, 1)]