from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert elements in T1 to integers
    int_list = [int(x) for x in T1]
    
    # Calculate the sum of the integers in T1
    total_sum = sum(int_list)
    
    # Generate a list of random integers with the length of total_sum
    random_integers = [randint(0, RANGE) for _ in range(total_sum)]
    
    # Count the occurrences of each number in the generated list
    count = Counter(random_integers)
    
    return count