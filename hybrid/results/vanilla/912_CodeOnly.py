from collections import Counter
import itertools

def task_func(letters: list, repetitions: int) -> dict:
    # Repeat the list of letters the specified number of times
    repeated_letters = list(itertools.chain.from_iterable(itertools.repeat(letters, repetitions)))
    
    # Count the frequency of each letter using Counter
    frequency_dict = Counter(repeated_letters)
    
    return dict(frequency_dict)

# Example usage:
# letters = ['a', 'b', 'c']
# repetitions = 3
# print(task_func(letters, repetitions))
# Output: {'a': 3, 'b': 3, 'c': 3}