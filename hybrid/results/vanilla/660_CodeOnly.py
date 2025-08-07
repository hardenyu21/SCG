import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(x, y, labels):
    # Ensure x and y are lists of arrays
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("x and y should be lists of arrays.")
    
    if not isinstance(labels, list):
        raise ValueError("labels should be a list of strings.")
    
    if len(x) != len(y) or len(x) != len(labels):
        raise ValueError("x, y, and labels should have the same length.")
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Iterate over each pair of x and y arrays
    for i in range(len(x)):
        # Reshape the arrays for scaling
        x_scaled = x[i].reshape(-1, 1)
        y_scaled = y[i].reshape(-1, 1)
        
        # Initialize the StandardScaler
        scaler = StandardScaler()
        
        # Fit and transform the data
        x_scaled = scaler.fit_transform(x_scaled).flatten()
        y_scaled = scaler.fit_transform(y_scaled).flatten()
        
        # Plot the scaled data
        ax.plot(x_scaled, y_scaled, label=labels[i])
    
    # Add labels and legend
    ax.set_xlabel('Scaled X')
    ax.set_ylabel('Scaled Y')
    ax.legend()
    
    # Return the figure object
    return fig