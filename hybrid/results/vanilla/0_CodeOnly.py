import itertools
from random import shuffle

def task_func(numbers=list(range(1, 3))):
    total_sum = 0
    num_permutations = 0
    
    # Generate all permutations of the list
    for perm in itertools.permutations(numbers):
        # Convert the permutation tuple to a list
        perm_list = list(perm)
        
        # Shuffle the list
        shuffle(perm_list)
        
        # Calculate the sum of absolute differences between consecutive numbers
        current_sum = sum(abs(perm_list[i] - perm_list[i + 1]) for i in range(len(perm_list) - 1))
        
        # Add to the total sum
        total_sum += current_sum
        
        # Increment the number of permutations
        num_permutations += 1
    
    # Calculate the average
    average = total_sum / num_permutations if num_permutations > 0 else 0
    
    return average

# Example usage:
# print(task_func([1, 2, 3, 4]))