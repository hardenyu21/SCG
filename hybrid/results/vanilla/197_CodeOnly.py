import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    # Calculate the absolute differences between the respective elements of l1 and l2
    differences = [abs(a - b) for a, b in zip(l1, l2)]
    
    # Find the N largest differences
    largest_differences = heapq.nlargest(N, differences)
    
    # Square the differences
    squared_differences = [diff ** 2 for diff in largest_differences]
    
    # Take the square root of the squared differences
    sqrt_differences = [math.sqrt(diff) for diff in squared_differences]
    
    # Plot the values
    fig, ax = plt.subplots()
    ax.plot(sqrt_differences, marker='o')
    ax.set_title('N Largest Differences')
    ax.set_xlabel('Index')
    ax.set_ylabel('Square Root of Squared Difference')
    
    # Return the Axes object
    return ax

# Example usage:
# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 4, 3, 2, 1]
# ax = task_func(l1, l2, N=3)
# plt.show()