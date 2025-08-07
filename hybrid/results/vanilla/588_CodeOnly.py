import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def task_func():
    # Generate random integers for 'X' and 'Y' columns
    data = {
        'X': np.random.randint(0, RANGE, SIZE),
        'Y': np.random.randint(0, RANGE, SIZE)
    }
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    # Plot the data using Seaborn
    sns.scatterplot(x='X', y='Y', data=df)
    plt.title('Scatter Plot of Random Integers')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    # Return the DataFrame
    return df

# Call the function to execute the task
task_func()