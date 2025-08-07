import pandas as pd
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    
    # Check if the DataFrame contains a 'job' column
    if 'job' not in data.columns:
        raise ValueError("DataFrame must contain a 'job' column.")
    
    # Count the occurrences of each job
    job_counts = data['job'].value_counts()
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(job_counts, labels=job_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Return the Figure object
    return fig