import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    try:
        # Load data from JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Check if data is empty
        if not data:
            return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data, columns=COLUMNS)
        
        # Calculate sum and mean for each email
        df['sum'] = df['list'].apply(np.sum)
        df['mean'] = df['list'].apply(np.mean)
        
        # Plot the sum and mean values
        fig, ax = plt.subplots()
        df.plot(kind='bar', x='email', y=['sum', 'mean'], ax=ax)
        ax.set_title('Sum and Mean of Lists for Each Email')
        ax.set_ylabel('Values')
        ax.set_xlabel('Email')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return df, ax
    
    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
    except json.JSONDecodeError:
        print(f"Error: The file {json_file} is not a valid JSON.")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean']), None

# Example usage:
# df, ax = task_func('emails.json')
# plt.show() if ax is not None else print("No data to plot.")