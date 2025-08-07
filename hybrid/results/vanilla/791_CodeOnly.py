from collections import Counter
import random
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l):
    # Move the first 3 elements to the end of the list
    l = l[3:] + l[:3]
    
    # Shuffle the list
    random.shuffle(l)
    
    # Create a cycled version of the list
    cycled_list = cycle(l)
    
    # Take the first 30 elements from the cycled list
    first_30_elements = [next(cycled_list) for _ in range(30)]
    
    # Create a frequency counter for the first 30 elements
    counter = Counter(first_30_elements)
    
    return counter

# Example usage
if __name__ == "__main__":
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    result = task_func(l)
    print(result)