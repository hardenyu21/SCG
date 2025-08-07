import collections
import random

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def task_func(animal_dict, max_count=10, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Reverse the dictionary
    reversed_dict = collections.defaultdict(list)
    for name, animal in animal_dict.items():
        reversed_dict[animal].append(name)
    
    # Convert defaultdict to a regular dictionary
    reversed_dict = dict(reversed_dict)
    
    # Count occurrences of each animal name with random counts
    animal_counter = {animal: random.randint(1, max_count) for animal in ANIMALS}
    
    return reversed_dict, animal_counter

# Example usage:
# animal_dict = {'Alice': 'Dog', 'Bob': 'Cat', 'Charlie': 'Dog', 'David': 'Elephant'}
# result = task_func(animal_dict)
# print(result)