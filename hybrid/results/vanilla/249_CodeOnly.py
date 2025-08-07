import pandas as pd
import random
from sklearn.model_selection import train_test_split

def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate random floating-point numbers within the specified range
    random_values = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_values = [round(value, 3) for value in random_values]
    
    # Create a DataFrame with the truncated values
    df = pd.DataFrame(truncated_values, columns=['Value'])
    
    # Split the data into train and test sets
    train_set, test_set = train_test_split(df, test_size=test_size, random_state=42)
    
    # Return the train and test sets as a tuple
    return train_set, test_set