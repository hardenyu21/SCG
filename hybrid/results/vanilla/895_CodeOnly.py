import numpy as np
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZE = 10000

def task_func():
    # Generate a numeric array of random integers between 1 and 100
    random_array = np.random.randint(1, 101, size=ARRAY_SIZE)
    
    # Calculate the mean and standard deviation
    mean_value = np.mean(random_array)
    std_deviation = np.std(random_array)
    
    # Create a histogram of the distribution
    fig, ax = plt.subplots()
    ax.hist(random_array, bins=range(1, 102), edgecolor='black', alpha=0.7)
    
    # Plot the mean as a red dashed line
    ax.axvline(mean_value, color='red', linestyle='--', label=f'Mean: {mean_value:.2f}')
    
    # Plot the standard deviation as purple dashed lines
    ax.axvline(mean_value - std_deviation, color='purple', linestyle='--', label=f'Std Dev: {std_deviation:.2f}')
    ax.axvline(mean_value + std_deviation, color='purple', linestyle='--')
    
    # Set the title and labels
    ax.set_title("Histogram of Random Values")
    ax.set_xlabel("Val")
    ax.set_ylabel("Freq")
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the tuple containing the array, mean, standard deviation, and the histogram plot
    return random_array, mean_value, std_deviation, ax

# Example usage
task_func()