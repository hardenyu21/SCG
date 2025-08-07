import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    try:
        # Load data from the specified table into a DataFrame
        query = f"SELECT age FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        
        # Check for negative age values
        if (df['age'] < 0).any():
            raise ValueError("The data contains negative age values.")
        
        # Plot the age distribution
        plt.figure(figsize=(10, 6))
        ax = sns.histplot(df['age'], bins=30, kde=True)
        ax.set_title('Age Distribution')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        
        # Return the Axes object
        return ax
    
    finally:
        # Close the database connection
        conn.close()