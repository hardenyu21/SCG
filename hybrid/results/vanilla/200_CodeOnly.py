import random
import statistics
import matplotlib.pyplot as plt

def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    random_numbers = [random.random() for _ in range(n)]
    
    # Calculate the average of the generated numbers
    average = statistics.mean(random_numbers)
    
    # Find numbers greater than the average
    greater_than_average = [num for num in random_numbers if num > average]
    
    # Count numbers greater than or equal to the specified value
    count_greater_or_equal = sum(1 for num in random_numbers if num >= value)
    
    # Sort the numbers
    sorted_numbers = sorted(random_numbers)
    
    # Plot the sorted numbers
    plt.plot(sorted_numbers, marker='o', linestyle='-')
    plt.title('Sorted Random Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()
    
    # Return the list of numbers greater than the average and the count
    return greater_than_average, count_greater_or_equal

# Example usage:
# result = task_func(100, 0.5)
# print("Numbers greater than average:", result[0])
# print("Count of numbers >= 0.5:", result[1])