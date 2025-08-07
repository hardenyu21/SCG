from collections import Counter
from operator import itemgetter
import itertools

# CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def task_func(animal_dict):
    # Filter the dictionary to only include keys that are in the ANIMAL constant
    filtered_dict = {animal: letters for animal, letters in animal_dict.items() if animal in ANIMAL}
    
    # Flatten the list of letters from the filtered dictionary
    all_letters = list(itertools.chain.from_iterable(filtered_dict.values()))
    
    # Count the frequency of each letter
    letter_counts = Counter(all_letters)
    
    # Sort the dictionary by frequency in descending order
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=itemgetter(1), reverse=True))
    
    return sorted_letter_counts

# Example usage:
# animal_dict = {
#     'cat': ['a', 't', 'c'],
#     'dog': ['d', 'o', 'g'],
#     'elephant': ['e', 'l', 'p', 'h', 'a', 'n', 't'],
#     'iguana': ['i', 'g', 'u', 'a', 'n', 'a'],
#     'jaguar': ['j', 'a', 'g', 'u', 'a', 'r']
# }
# print(task_func(animal_dict))