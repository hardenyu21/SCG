import collections
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length from the predefined list of letters
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))
    
    # Count the frequency of each letter in the generated string
    frequency_counter = collections.Counter(random_string)
    
    # Sort the frequency counter by frequency in descending order
    sorted_frequency = sorted(frequency_counter.items(), key=lambda item: item[1], reverse=True)
    
    # Create an ordered dictionary from the sorted frequency list
    ordered_frequency_dict = collections.OrderedDict(sorted_frequency)
    
    return ordered_frequency_dict

# Example usage
if __name__ == "__main__":
    result = task_func(100)
    print(result)