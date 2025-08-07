import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_labels=5, data_range=(0, 1)):
    # Generate random data
    data = np.random.randint(data_range[0], data_range[1] + 1, size=(num_labels, num_labels))
    
    # Create a DataFrame for better visualization
    df = pd.DataFrame(data, columns=[f'Category {i+1}' for i in range(num_labels)])
    
    # Plotting the stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    
    # Setting labels and title
    ax.set_xlabel('Labels')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Data')
    
    # Show the plot
    plt.tight_layout()
    
    return fig

# Example usage
fig = task_func(num_labels=3, data_range=(1, 10))
fig.show()  # This will display the figure with three labels and data range from 1 to 10