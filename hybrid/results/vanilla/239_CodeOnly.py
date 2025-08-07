import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def task_func(original):
    # Extract numeric values from the list of tuples
    numeric_values = []
    for item in original:
        if isinstance(item, tuple):
            for element in item:
                if isinstance(element, (int, float)):
                    numeric_values.append(element)
    
    # Convert the list to a numpy array
    numeric_array = np.array(numeric_values)
    
    # Compute basic statistics
    basic_stats = {
        'mean': np.mean(numeric_array),
        'std_dev': np.std(numeric_array),
        'min': np.min(numeric_array),
        'max': np.max(numeric_array)
    }
    
    # Plot histogram with overlaid PDF
    fig, ax = plt.subplots()
    count, bins, ignored = ax.hist(numeric_array, bins='auto', density=True, alpha=0.6, color='g')
    
    # Fit a normal distribution to the data
    mu, std = stats.norm.fit(numeric_array)
    
    # Plot the PDF
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    ax.plot(x, p, 'k', linewidth=2)
    
    # Add labels and title
    ax.set_title('Histogram with Overlaid PDF')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    
    # Return the results
    return numeric_array, basic_stats, ax

# Example usage:
# original_data = [(1, 2, 'a'), (3.5, 4), (5, 'b', 6.7)]
# numeric_array, basic_stats, ax = task_func(original_data)
# plt.show()