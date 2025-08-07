import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_func(db_name, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    try:
        # Query the table to get column names and data types
        query = f"PRAGMA table_info({table_name})"
        df_info = pd.read_sql_query(query, conn)
        
        # Filter out non-numeric columns and the 'id' column
        numeric_columns = df_info[df_info['type'].isin(['INTEGER', 'REAL', 'FLOAT', 'NUMERIC'])]
        numeric_columns = numeric_columns[numeric_columns['name'] != 'id']
        
        # Check if there are at least two numeric columns
        if len(numeric_columns) < 2:
            raise ValueError("The table has less than two numerical columns.")
        
        # Get the first two numeric column names
        col1, col2 = numeric_columns['name'].iloc[0], numeric_columns['name'].iloc[1]
        
        # Query the table to get the data for these columns
        query = f"SELECT {col1}, {col2} FROM {table_name}"
        df_data = pd.read_sql_query(query, conn)
        
        # Plot the scatterplot
        fig, ax = plt.subplots()
        ax.scatter(df_data[col1], df_data[col2])
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        ax.set_title(f'Scatterplot of {col1} vs {col2}')
        
        # Return the Axes object
        return ax
    
    finally:
        # Close the database connection
        conn.close()