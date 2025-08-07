from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    # Flatten the list of words into a single string of letters
    all_letters = ''.join(word_dict.keys())
    
    # Use Counter to count the frequency of each letter
    letter_frequency = Counter(all_letters)
    
    # Convert the Counter object to a dictionary and return it
    return dict(letter_frequency)

# Example usage:
word_dict = {
    'apple': 'a',
    'banana': 'b',
    'cherry': 'c',
    'date': 'd'
}

print(task_func(word_dict))