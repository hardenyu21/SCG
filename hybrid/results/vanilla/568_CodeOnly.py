import inspect
import matplotlib.pyplot as plt
import pandas as pd

def task_func(f_list):
    # Check for lambda functions and raise ValueError if any are found
    for f in f_list:
        if isinstance(f, type(lambda: None)) and f.__name__ == "<lambda>":
            raise ValueError("Input contains a lambda function.")
    
    # Extract function names and their number of arguments
    data = []
    for f in f_list:
        if callable(f):
            num_args = len(inspect.signature(f).parameters)
            data.append({'Function Name': f.__name__, 'Number of Arguments': num_args})
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Function Name'], df['Number of Arguments'], color='skyblue')
    plt.xlabel('Function Name')
    plt.ylabel('Number of Arguments')
    plt.title('Number of Arguments for Each Function')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Return the DataFrame
    return df