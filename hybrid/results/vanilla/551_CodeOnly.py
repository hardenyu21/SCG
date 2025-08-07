from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def task_func(list_of_menuitems):
    # Flatten the nested list
    def flatten(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    # Flatten the list of menu items
    flat_list = list(flatten(list_of_menuitems))

    # Count the frequency of each menu item
    item_counts = Counter(flat_list)

    # If there are no items to plot, return None
    if not item_counts:
        return None

    # Create a DataFrame from the item counts
    df = pd.DataFrame(item_counts.items(), columns=['MenuItem', 'Frequency'])

    # Create a seaborn barplot
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='MenuItem', y='Frequency', data=df, palette='viridis')

    # Set plot labels and title
    ax.set_xlabel('Menu Item')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Menu Items')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()

    # Return the Axes object
    return ax