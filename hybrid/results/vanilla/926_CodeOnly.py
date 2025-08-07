import pandas as pd
import sqlite3

def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    try:
        # Load data from the specified table into a DataFrame
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        
        # Check if the specified column exists in the DataFrame
        if column_name in df.columns:
            # Replace newline characters with HTML line break tags in the specified column
            df[column_name] = df[column_name].str.replace('\n', '<br>', regex=False)
        else:
            raise ValueError(f"Column '{column_name}' does not exist in the table '{table_name}'.")
        
    finally:
        # Close the database connection
        conn.close()
    
    # Return the modified DataFrame
    return df