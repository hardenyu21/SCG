import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Combine the lists into a single 2D array
    data = np.array([a, b]).T
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the standardized values
    df = pd.DataFrame(standardized_data, columns=columns)
    
    # Plot the standardized values using a bar plot
    ax = df.plot(kind='bar', figsize=(10, 6))
    ax.set_title('Standardized Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# a = [1, 2, 3, 4, 5]
# b = [5, 4, 3, 2, 1]
# df, ax = task_func(a, b)