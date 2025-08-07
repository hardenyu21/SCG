import collections
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(dictionary, new_key, new_value):
    # Add the new key-value pair to the dictionary
    dictionary[new_key] = new_value
    
    # Count the frequency of each value in the dictionary
    value_counts = collections.Counter(dictionary.values())
    
    # Plot the distribution of the values
    fig, ax = plt.subplots()
    sns.barplot(x=list(value_counts.keys()), y=list(value_counts.values()), ax=ax)
    ax.set_title('Distribution of Dictionary Values')
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the updated dictionary and the axes object
    return dictionary, ax

# Example usage:
# updated_dict, ax = task_func({'a': 1, 'b': 2, 'c': 1}, 'd', 3)