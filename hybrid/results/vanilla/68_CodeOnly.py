import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the DataFrame where 'Employee ID' starts with the given prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Select only the 'Employee ID' and 'Age' columns
    filtered_df = filtered_df[['Employee ID', 'Age']]
    
    # Draw a histogram of the 'Age' column
    ax = sns.histplot(filtered_df['Age'], bins=10, kde=True)
    plt.title('Age Distribution of Employees with ID Prefix "{}"'.format(emp_prefix))
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    # Return the filtered DataFrame and the Axes object
    return filtered_df, ax

# Example usage:
# df, ax = task_func('/path/to/data.csv', 'EMP')