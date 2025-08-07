import numpy as np
import statistics
import matplotlib.pyplot as plt

def task_func(data, value):
    # Check if the data list is empty
    if not data:
        return np.array([]), 0
    
    # Calculate the average of the data
    average = statistics.mean(data)
    
    # Identify values greater than the average
    greater_than_average = [x for x in data if x > average]
    
    # Count how many values are greater than the specified value
    count_greater_than_value = sum(1 for x in data if x > value)
    
    # Convert the list to a numpy array
    greater_than_average_array = np.array(greater_than_average)
    
    # Sort the data for plotting
    sorted_data = sorted(data)
    
    # Plot the histogram of the sorted numbers
    plt.hist(sorted_data, bins='auto', alpha=0.7, color='blue')
    plt.title('Histogram of Sorted Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
    return greater_than_average_array, count_greater_than_value

# Example usage:
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# value = 5
# result = task_func(data, value)
# print(result)