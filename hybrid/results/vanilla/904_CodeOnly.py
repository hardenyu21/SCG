import pandas as pd
import matplotlib.pyplot as plt

def task_func(d, keys=['x', 'y', 'z']):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(d)
    
    # Check if the specified keys exist in the DataFrame
    for key in keys:
        if key not in df.columns:
            raise ValueError(f"Key '{key}' not found in the data.")
    
    # Plot the specified keys
    ax = df.plot(x=keys[0], y=keys[1:], kind='line', marker='o')
    
    # Set labels and title
    ax.set_xlabel(keys[0])
    ax.set_ylabel('Values')
    ax.set_title('Plot of specified keys')
    
    # Return the Matplotlib Axes object
    return ax