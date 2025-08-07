import numpy as np
import matplotlib.pyplot as plt

def task_func():
    # Define the range of x values
    x_values = np.linspace(-10, 10, 400)
    
    # Calculate the corresponding y values for the equation y = 2x + 1
    y_values = 2 * x_values + 1
    
    # Create the plot
    fig, ax = plt.subplots()
    
    # Plot the line for the equation y = 2x + 1
    ax.plot(x_values, y_values, 'r-', label='y=2x+1')
    
    # Mark the solution at x = 2 with a green circle
    solution_x = 2
    solution_y = 2 * solution_x + 1
    ax.plot(solution_x, solution_y, 'go', label='Solution at x=2')
    
    # Set the title and labels
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Set the x-axis range
    ax.set_xlim(-10, 10)
    
    # Automatically adjust the y-axis range
    ax.set_ylim(min(y_values), max(y_values))
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax

# Call the function to display the plot
task_func()