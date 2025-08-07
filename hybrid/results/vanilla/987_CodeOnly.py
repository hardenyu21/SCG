import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Extract numerical data using the provided key
        if data_key not in data:
            raise KeyError(f"Key '{data_key}' not found in the JSON data.")
        
        # Convert the extracted data to a pandas Series
        original_data = pd.Series(data[data_key], dtype='float64')
        
        # Check if the data is empty
        if original_data.empty:
            return original_data, None, None
        
        # Min-Max normalize the data
        scaler = MinMaxScaler()
        normalized_data = pd.Series(scaler.fit_transform(original_data.values.reshape(-1, 1)).flatten(), dtype='float64')
        
        # Create a line plot
        fig, ax = plt.subplots()
        ax.plot(original_data.index, original_data, label='Original Data', marker='o')
        ax.plot(normalized_data.index, normalized_data, label='Normalized Data', marker='x')
        
        # Set plot title and labels
        ax.set_title('Comparison of Original and Normalized Data')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.legend()
        
        # Return the results
        return original_data, normalized_data, ax
    
    except KeyError as e:
        raise KeyError(str(e))
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None