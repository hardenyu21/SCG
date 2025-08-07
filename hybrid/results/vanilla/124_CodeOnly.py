from random import randint, seed as random_seed
import time
import matplotlib.pyplot as plt

def task_func(my_list, size=100, seed=100):
    # Validate input
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list.")
    if not all(isinstance(x, (int, float)) for x in my_list):
        raise ValueError("All elements in my_list must be numeric (int or float).")
    
    # Append the number 12 to my_list
    my_list.append(12)
    
    # Calculate the sum of elements in my_list
    total_sum = sum(my_list)
    
    # Determine the size of the random numbers list
    list_size = min(total_sum, size)
    
    # Set the random seed for reproducibility
    random_seed(seed)
    
    # Start timing
    start_time = time.time()
    
    # Generate a list of random integers
    random_numbers = [randint(1, 100) for _ in range(list_size)]
    
    # End timing
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(random_numbers, bins=range(1, 102), edgecolor='black', align='left')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    
    # Return the time taken and the Axes object
    return time_taken, ax

# Example usage:
# time_taken, ax = task_func([1, 2, 3], size=50)
# plt.show()