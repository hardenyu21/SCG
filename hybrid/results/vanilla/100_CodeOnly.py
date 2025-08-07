import matplotlib.pyplot as plt
import pandas as pd
import random
from datetime import datetime, timedelta

def task_func(seed=42):
    try:
        # Set the random seed for reproducibility
        random.seed(seed)
        
        # Generate dates for the past 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=29)
        dates = [start_date + timedelta(days=i) for i in range(30)]
        
        # Generate random time series data
        values = [random.uniform(0, 100) for _ in range(30)]
        
        # Create a DataFrame
        df = pd.DataFrame({'Date': dates, 'Value': values})
        
        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['Value'], marker='o')
        
        # Set plot labels and title
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        ax.set_title('Random Time Series Data')
        
        # Set font to Arial
        plt.rcParams['font.family'] = 'Arial'
        
        # Show the plot
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return ax
    
    except Exception as e:
        raise ValueError(f"An error occurred while generating the data or plot: {e}")

# Example usage:
# ax = task_func(seed=42)