import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns are present in the DataFrame
    if 'Age' not in df.columns or 'Weight' not in df.columns:
        raise KeyError("The input DataFrame must contain the columns 'Age' and 'Weight'.")
    
    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # If the filtered DataFrame is empty, return it as is
    if filtered_df.empty:
        return filtered_df
    
    # Select only the numerical columns for standardization
    numerical_cols = filtered_df.select_dtypes(include=['number']).columns
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the numerical columns
    filtered_df[numerical_cols] = scaler.fit_transform(filtered_df[numerical_cols])
    
    return filtered_df