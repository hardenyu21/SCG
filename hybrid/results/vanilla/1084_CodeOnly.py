import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

def task_func(data_file_path: str):
    # Read the CSV file
    df = pd.read_csv(data_file_path)
    
    # Convert string representations of numbers with commas into floating point numbers
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '').astype(float)
    
    # Calculate mean and standard deviation for each numerical column
    means = df.mean()
    std_devs = df.std()
    
    # Generate histogram plots for each numerical column
    axes = []
    fig, axs = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(8, 4 * len(df.columns)))
    if len(df.columns) == 1:
        axs = [axs]  # Ensure axs is iterable
    
    for i, col in enumerate(df.columns):
        ax = axs[i]
        df[col].hist(ax=ax, bins=10, edgecolor='black')
        ax.set_title(f'Histogram of {col}')
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    # Perform ANOVA test to check the statistical significance of differences between means of numerical columns
    anova_results = pd.DataFrame(columns=['Column1', 'Column2', 'F-value', 'P-value'])
    
    if len(df.columns) > 1:
        for i in range(len(df.columns)):
            for j in range(i + 1, len(df.columns)):
                col1 = df.columns[i]
                col2 = df.columns[j]
                f_value, p_value = f_oneway(df[col1], df[col2])
                anova_results = anova_results.append({
                    'Column1': col1,
                    'Column2': col2,
                    'F-value': f_value,
                    'P-value': p_value
                }, ignore_index=True)
    
    # Show the plots
    plt.tight_layout()
    plt.show()
    
    return means, std_devs, axes, anova_results