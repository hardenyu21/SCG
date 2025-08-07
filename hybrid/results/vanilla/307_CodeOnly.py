import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Fill empty sublists with 5 random integers ranging from 0 to 100
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend(random.randint(0, 100) for _ in range(5))
    
    # Combine all sublists into a single list
    combined_data = [item for sublist in list_of_lists for item in sublist]
    
    # Create a histogram using seaborn
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(combined_data, bins=20, kde=True)
    
    # Set plot title and labels
    ax.set_title('Histogram of Combined Data')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax