import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    # Convert the input dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        try:
            # Try to convert the column to float
            df[column] = df[column].astype(float)
            # Scale the column if it is numeric
            df[column] = scaler.fit_transform(df[[column]])
        except ValueError:
            # If conversion to float fails, leave the column unchanged
            continue
    
    return df