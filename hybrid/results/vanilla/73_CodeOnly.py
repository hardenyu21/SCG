import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

def task_func(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Load data from the EmailData table
    query = "SELECT email, list FROM EmailData"
    df = pd.read_sql_query(query, conn)
    
    # Convert the string representation of the list into actual lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and variance for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    
    # Close the database connection
    conn.close()
    
    # Plot the sum, mean, and variance
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='bar', x='email', y=['sum', 'mean', 'var'], ax=ax)
    ax.set_title('Sum, Mean, and Variance of Email Lists')
    ax.set_ylabel('Values')
    ax.set_xlabel('Email')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the DataFrame and the Axes object
    return df, ax

# Example usage:
# df, ax = task_func('path_to_your_database.db')
# plt.show()