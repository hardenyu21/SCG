import sys
import sqlite3

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    # Append the path to sys.path if it's not already there
    if path_to_append not in sys.path:
        sys.path.append(path_to_append)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paths (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE
        )
    ''')
    
    # Insert the path into the database, avoiding duplicates
    try:
        cursor.execute('INSERT INTO paths (path) VALUES (?)', (path_to_append,))
        conn.commit()
    except sqlite3.IntegrityError:
        # Path already exists in the database
        pass
    
    # Close the database connection
    conn.close()
    
    # Return the path that was appended and inserted
    return path_to_append

# Example usage
if __name__ == "__main__":
    result = task_func()
    print(f"Path appended and inserted: {result}")