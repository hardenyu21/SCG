from collections import Counter
import itertools

def task_func(d):
    # Flatten all lists in the dictionary into a single iterable
    all_values = itertools.chain.from_iterable(d.values())
    
    # Use Counter to count occurrences of each integer
    counts = Counter(all_values)
    
    # Convert Counter object to a regular dictionary and return
    return dict(counts)