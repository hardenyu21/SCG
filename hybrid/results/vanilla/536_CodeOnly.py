import sqlite3
import pandas as pd
import os

def task_func(db_name, table_name, csv_path="data.csv"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    try:
        # Read the table into a pandas DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # Export the DataFrame to a CSV file
        df.to_csv(csv_path, index=False)
        
        # Get the absolute path of the exported CSV file
        absolute_path = os.path.abspath(csv_path)
        
        return absolute_path
    
    finally:
        # Close the database connection
        conn.close()