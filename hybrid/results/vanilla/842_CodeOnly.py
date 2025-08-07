import sqlite3
import random

def task_func(db_path,
              num_entries,
              users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        random.seed(random_seed)
    
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create the 'users' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            country TEXT NOT NULL
        )
    ''')
    
    # Insert random user data into the 'users' table
    for _ in range(num_entries):
        name = random.choice(users)
        age = random.randint(20, 60)
        country = random.choice(countries)
        c.execute('INSERT INTO users (name, age, country) VALUES (?, ?, ?)', (name, age, country))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the file path of the generated SQLite database
    return db_path

# Example usage
path = task_func('test.db', num_entries=3, random_seed=2, users=['Simon', 'Albert'])
print(path)