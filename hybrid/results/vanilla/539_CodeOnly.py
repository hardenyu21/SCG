import sqlite3
from random import choice, randint, seed
import os

def task_func(db_name, table_name, num_entries, random_seed=None):
    # Validate num_entries
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative.")
    
    # Constants for random data
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 66)
    HEIGHTS = range(150, 201)
    
    # Set random seed if provided
    if random_seed is not None:
        seed(random_seed)
    
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            name TEXT,
            age INTEGER,
            height INTEGER
        )
    ''')
    
    # Insert random data into the table
    for _ in range(num_entries):
        name = choice(NAMES)
        age = randint(18, 65)
        height = randint(150, 200)
        cursor.execute(f'''
            INSERT INTO {table_name} (name, age, height)
            VALUES (?, ?, ?)
        ''', (name, age, height))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the absolute path of the database file
    return os.path.abspath(db_name)

# Example usage:
# db_path = task_func('example.db', 'people', 10, random_seed=42)
# print(f"Database created at: {db_path}")