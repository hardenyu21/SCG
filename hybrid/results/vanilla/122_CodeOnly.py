import numpy as np
import random

def task_func(my_list):
    # Append a randomly selected integer between 0 and 100 to the list
    random_integer = random.randint(0, 100)
    my_list.append(random_integer)
    
    # Calculate the sum of the numbers in the modified list
    total_sum = sum(my_list)
    
    # Generate a numpy array of random floating-point numbers with the size of total_sum
    random_array = np.random.rand(total_sum)
    
    return random_array