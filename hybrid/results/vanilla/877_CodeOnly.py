import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    # Check if the input is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data is not a DataFrame.")
    
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("Input data is empty.")
    
    # Check if all columns in the DataFrame are numeric
    if not all(data.dtypes.apply(lambda x: pd.api.types.is_numeric_dtype(x))):
        raise ValueError("Input data contains non-numeric data.")
    
    # Check if n_components is greater than the number of columns
    if n_components > data.shape[1]:
        raise ValueError("n_components is greater than the number of columns in the data.")
    
    # Scale the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    # Apply PCA
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    
    # Create a new DataFrame with the principal components
    columns = [f'PC{i+1}' for i in range(n_components)]
    result_df = pd.DataFrame(principal_components, columns=columns)
    
    return result_df