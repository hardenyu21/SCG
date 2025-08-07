import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize lists to store time and random numbers
    times = []
    random_numbers = []
    
    # Start the timer
    start_time = time.time()
    
    for i in range(intervals):
        # Generate a random number
        random_number = random.random()
        
        # Record the current elapsed time
        elapsed_time = time.time() - start_time
        
        # Append the time and random number to their respective lists
        times.append(elapsed_time)
        random_numbers.append(random_number)
        
        # Wait for 1 second
        time.sleep(1)
    
    # Plot the random numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(times, random_numbers, marker='o', linestyle='-')
    ax.set_xlabel('Elapsed Time (s)')
    ax.set_ylabel('Random Number')
    ax.set_title('Random Numbers Over Time')
    
    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(random_numbers)
    
    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value

# Example usage:
# ax, kurtosis_value = task_func(intervals=10, seed=42)
# plt.show()
# print(f"Kurtosis: {kurtosis_value}")