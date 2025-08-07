import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    # Fit and transform the data using LabelEncoder
    encoded_data = label_encoder.fit_transform(data)
    
    # Create a DataFrame with the original and encoded data
    df = pd.DataFrame({
        'Category': data,
        'Encoded': encoded_data
    })
    
    return df

# Example usage:
# data = ['apple', 'banana', 'orange', 'apple', 'orange']
# df = task_func(data)
# print(df)