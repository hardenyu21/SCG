import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(num_samples=100, num_features=5):
    # Generate a DataFrame with random values
    data = np.random.rand(num_samples, num_features)
    columns = [f'Feature_{i+1}' for i in range(num_features)]
    df = pd.DataFrame(data, columns=columns)
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Visualize the correlation matrix using a heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Heatmap')
    plt.show()
    
    return df, ax

# Example usage
df, ax = task_func()