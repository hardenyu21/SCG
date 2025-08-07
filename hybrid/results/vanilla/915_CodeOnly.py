import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the Z-Scores for the 'closing_price' column
    df['z_score'] = zscore(df['closing_price'])
    
    # Identify outliers based on the Z-Score threshold
    outliers = df[np.abs(df['z_score']) > z_threshold]
    
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df.index, df['closing_price'], label='Closing Price', marker='o')
    ax.scatter(outliers.index, outliers['closing_price'], color='red', label='Outliers', zorder=5)
    
    # Highlight outliers on the plot
    for index, row in outliers.iterrows():
        ax.annotate(f'Z={row["z_score"]:.2f}', (index, row['closing_price']), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Set plot labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()
    
    # Remove the z_score column before returning
    df.drop(columns='z_score', inplace=True)
    
    return outliers[['closing_price']], ax

# Example usage
df2 = pd.DataFrame({
    'closing_price': [10, 20, 30, 40, 50, 100]
})
outliers2, plot2 = task_func(df2, z_threshold=1.5)
plt.show()