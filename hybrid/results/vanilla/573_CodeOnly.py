import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(array_length=100):
    # Generate two arrays of random numbers
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)
    
    # Calculate statistics for each array
    mean1 = np.mean(array1)
    median1 = np.median(array1)
    std_dev1 = np.std(array1)
    
    mean2 = np.mean(array2)
    median2 = np.median(array2)
    std_dev2 = np.std(array2)
    
    # Create a DataFrame to store the statistics
    statistics = pd.DataFrame({
        'Array1': [mean1, median1, std_dev1],
        'Array2': [mean2, median2, std_dev2]
    }, index=['Mean', 'Median', 'Standard Deviation'])
    
    # Plot a bar chart to compare the statistics
    ax = statistics.plot(kind='bar', figsize=(10, 6))
    ax.set_title('Comparison of Statistics for Two Random Arrays')
    ax.set_ylabel('Value')
    ax.set_xlabel('Statistics')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    return statistics, ax

# Example usage
df, ax = task_func(100)