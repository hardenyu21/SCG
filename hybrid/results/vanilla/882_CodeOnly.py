import sqlite3
import pandas as pd
import os
import re

def task_func(db_file, table_name, column_name, pattern=r'\d+[xX]'):
    # Check if the database file exists
    if not os.path.exists(db_file):
        raise ValueError("The database file does not exist.")
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    try:
        # Query to select all entries from the specified table
        query = f"SELECT {column_name} FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        
        # Function to find matches in a single string
        def find_matches(text):
            if pd.isna(text):
                return []
            return re.findall(pattern, text)
        
        # Apply the find_matches function to the specified column
        df['matches'] = df[column_name].apply(find_matches)
        
        # Explode the matches list into separate rows
        matches_df = df.explode('matches').dropna(subset=['matches'])
        
        return matches_df
    
    finally:
        # Close the database connection
        conn.close()