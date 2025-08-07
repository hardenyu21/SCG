import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Generate x values from -10 to 10 with 400 points
    x = np.linspace(-10, 10, 400)
    # Calculate y values using the equation y = x^2
    y = x**2
    
    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='y = x^2')
    
    # Set the title and labels
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Enable the grid
    plt.grid(True)
    
    # Show the plot
    plt.legend()
    plt.show()

# Call the function to display the plot
task_func()