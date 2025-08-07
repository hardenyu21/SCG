import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_diabetes

def task_func():
    # Set the font to Arial
    plt.rcParams['font.family'] = 'Arial'
    
    # Load the diabetes dataset
    diabetes = load_diabetes()
    
    # Create a DataFrame from the dataset
    diabetes_df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
    diabetes_df['target'] = diabetes.target
    
    # Create a pairplot using seaborn
    pairplot = sns.pairplot(diabetes_df)
    
    # Get the current figure
    fig = pairplot.fig
    
    # Return the figure and the DataFrame
    return fig, diabetes_df

# Example usage
fig, diabetes_df = task_func()
plt.show()