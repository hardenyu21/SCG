import itertools
import statistics

def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate the mean of the subset sums
    mean_value = statistics.mean(subset_sums)
    
    # Calculate the median of the subset sums
    median_value = statistics.median(subset_sums)
    
    # Calculate the mode of the subset sums
    try:
        mode_value = statistics.mode(subset_sums)
    except statistics.StatisticsError:
        mode_value = None  # In case there is no unique mode
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }

# Example usage:
# elements = (1, 2, 3, 4)
# subset_size = 2
# result = task_func(elements, subset_size)
# print(result)