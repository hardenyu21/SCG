from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Helper function to flatten the nested list
    def flatten(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    # Flatten the list of menu items
    flat_list = list(flatten(list_of_menuitems))
    
    # Count the occurrences of each menu item
    item_counts = Counter(flat_list)
    
    # Create a DataFrame from the counter
    df = pd.DataFrame.from_dict(item_counts, orient='index', columns=['Count'])
    
    # Rename the index to 'MenuItem'
    df.index.name = 'MenuItem'
    
    return df