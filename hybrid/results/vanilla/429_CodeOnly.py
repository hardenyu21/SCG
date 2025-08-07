import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df1, df2):
    # Ensure the dataframes are combined and the target is separated
    combined_df = pd.concat([df1, df2], axis=1)
    X = combined_df.drop(columns='target')  # Assuming 'target' is the column name for the target variable
    y = combined_df['target']
    
    # Perform feature selection using SelectKBest
    selector = SelectKBest(score_func=f_classif, k=2)
    X_new = selector.fit_transform(X, y)
    
    # Get the mask of selected features
    mask = selector.get_support()
    
    # Get the list of selected feature names
    selected_features = X.columns[mask].tolist()
    
    # Create a correlation matrix for the selected features
    selected_df = X[selected_features]
    corr_matrix = selected_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Selected Features')
    plt.show()
    
    return selected_features, ax

# Example usage:
# df1 = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'feature3': [7, 8, 9]})
# df2 = pd.DataFrame({'target': [0, 1, 0]})
# selected_features, ax = task_func(df1, df2)