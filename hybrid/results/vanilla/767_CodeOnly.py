from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    # Replace each sublist with a random letter
    random_letters = [random.choice(LETTERS) for _ in list_of_lists]
    
    # Count each letter in the final list
    letter_count = Counter(random_letters)
    
    return dict(letter_count)

# Example usage:
# nested_list = [[1, 2], [3, 4], [5, 6]]
# print(task_func(nested_list))