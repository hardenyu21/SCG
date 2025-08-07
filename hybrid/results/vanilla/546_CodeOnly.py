from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    # Sort the dictionary by keys
    sorted_dict = OrderedDict(sorted(my_dict.items()))
    
    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Key", "Value"]
    
    # Add rows to the table
    for key, value in sorted_dict.items():
        table.add_row([key, value])
    
    return table

# Example usage
if __name__ == "__main__":
    print(task_func({}))