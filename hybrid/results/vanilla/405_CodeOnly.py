import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate a list of random numbers
    random_numbers = [random.random() for _ in range(points)]
    
    # Create a plot
    fig, ax = plt.subplots()
    ax.plot(range(points), random_numbers, marker='o')
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Random Number')
    ax.set_title('Plot of Random Numbers')
    
    # Show the plot
    plt.show()
    
    # Return the list of random numbers and the Axes object
    return random_numbers, ax

# Example usage:
# random_numbers, ax = task_func(10)