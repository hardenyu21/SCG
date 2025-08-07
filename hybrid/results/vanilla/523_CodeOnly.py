import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        return None
    
    # Combine the list of dictionaries into a single dictionary
    combined_data = {}
    for d in data:
        for key, value in d.items():
            if key in combined_data:
                combined_data[key].append(value)
            else:
                combined_data[key] = [value]
    
    # Convert the combined dictionary into a Pandas DataFrame
    df = pd.DataFrame(combined_data)
    
    # Plot the data
    ax = df.plot(title='Data over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Data Points')
    
    # Show the plot
    plt.show()
    
    return ax