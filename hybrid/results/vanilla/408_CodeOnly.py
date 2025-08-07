import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    try:
        # Execute the query and fetch the results into a DataFrame
        df = pd.read_sql_query(query, conn)
    finally:
        # Ensure the connection is closed
        conn.close()
    
    # Return the DataFrame containing the query results
    return df