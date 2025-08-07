from scipy import stats
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Extract the data series from the dictionary using the provided keys
    series1 = data_dict[data_keys[0]]
    series2 = data_dict[data_keys[1]]
    
    # Calculate the correlation coefficient
    correlation_coefficient, _ = stats.pearsonr(series1, series2)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(series1, series2)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Scatter Plot of {data_keys[0]} vs {data_keys[1]}')
    
    # Return the correlation coefficient and the Axes object
    return correlation_coefficient, ax

# Example usage:
# data_dict = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
# data_keys = ['A', 'B']
# correlation, ax = task_func(data_dict, data_keys)
# plt.show()