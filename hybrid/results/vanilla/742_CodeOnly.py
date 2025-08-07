import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    # Check if the input list is empty
    if not list_of_pairs:
        raise Exception("The input array is empty.")
    
    # Extract categories and values from the list of pairs
    categories = []
    values = []
    
    for category, value in list_of_pairs:
        categories.append(category)
        # Check if the value is numeric
        if not isinstance(value, (int, float)):
            raise ValueError("Values are not numeric.")
        values.append(value)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Normalize the 'Value' column using MinMaxScaler
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df