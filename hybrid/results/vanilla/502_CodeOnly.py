from datetime import datetime, timedelta
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(days_in_past=7, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Define the activities
    activities = ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"]
    
    # Generate a list of dates in the past
    dates = [datetime.now() - timedelta(days=i) for i in range(days_in_past)]
    
    # Create a list to store the data
    data = []
    
    # Generate random data for each date and activity
    for date in dates:
        for activity in activities:
            duration = random.randint(0, 120)
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Activity': activity,
                'Duration': duration
            })
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Plot the data using Seaborn
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(data=df, x='Date', y='Duration', hue='Activity', marker='o')
    ax.set_title('Daily Activity Durations')
    ax.set_xlabel('Date')
    ax.set_ylabel('Duration (minutes)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the Axes object and the DataFrame
    return ax, df

# Example usage
ax, df = task_func(days_in_past=7, random_seed=0)
plt.show()