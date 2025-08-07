import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(num_groups=5, data_size=5, labels=None):
    # Generate random data
    np.random.seed(0)  # For reproducibility
    data = np.random.randint(1, 100, size=(data_size, num_groups))
    
    # Create a DataFrame
    if labels is None:
        labels = [f'Category {i+1}' for i in range(num_groups)]
    df = pd.DataFrame(data, columns=labels)
    
    # Plotting
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Stacked Bar Chart of Random Data')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Values')
    ax.legend(title='Categories')
    
    # Save the plot to a file
    filename = 'test_plot.png'
    plt.savefig(filename)
    
    # Return the Figure object, DataFrame, and filename
    return fig, df, filename

# Example usage
fig, df, filename = task_func()
print(f"DataFrame:\n{df}")
print(f"Plot saved to: {filename}")