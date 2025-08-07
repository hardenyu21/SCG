import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def task_func(num_rows=5, rand_range=(0, 100)):
    # Create a DataFrame with random integer values for categories 'A' through 'E'
    data = {
        'A': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'B': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'C': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'D': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)],
        'E': [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)]
    }
    df = pd.DataFrame(data)
    
    # Plot the data using a stacked bar chart
    fig, ax = plt.subplots()
    df.plot(kind='bar', stacked=True, ax=ax)
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('Stacked Bar Chart of Random Integer Values')
    
    # Show the plot
    plt.tight_layout()
    
    return fig

# Example usage:
# fig = task_func(num_rows=10, rand_range=(0, 200))
# plt.show()