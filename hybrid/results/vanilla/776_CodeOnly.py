import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(file_path, output_path=None, sort_key='title', linear_regression=False, x_column=None, y_column=None):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Sort the DataFrame by the specified column key
        df_sorted = df.sort_values(by=sort_key)
        
        # Check if linear regression is required
        if linear_regression:
            # Check if the specified columns exist in the DataFrame
            if x_column not in df_sorted.columns or y_column not in df_sorted.columns:
                raise ValueError("Specified columns for linear regression do not exist in the dataframe")
            
            # Prepare the data for linear regression
            X = df_sorted[[x_column]].values
            y = df_sorted[y_column].values
            
            # Fit the linear regression model
            model = LinearRegression()
            model.fit(X, y)
            
            # Return the fitted model
            return model
        
        # If output_path is provided, write the sorted DataFrame to a new CSV file
        if output_path:
            df_sorted.to_csv(output_path, index=False)
            return output_path
        
        # If no output_path is provided, return the sorted DataFrame
        return df_sorted
    
    except Exception as e:
        raise Exception(f"An error occurred: {e}")