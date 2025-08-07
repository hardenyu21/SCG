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
import unittest
import sqlite3
import os
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir_path = self.temp_dir.name
        self.db_name = "test_function.db"
        self.db_path = os.path.join(self.temp_dir_path, self.db_name)
        self.table_name = "TestTable"
        self.random_seed = 42
    def tearDown(self):
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Test basic case
        num_entries = 5
        db_path = task_func(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_2(self):
        # Test handling 0 entries
        num_entries = 0
        db_path = task_func(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_3(self):
        # Test handling 1 entry
        num_entries = 1
        db_path = task_func(
            self.db_path, self.table_name, num_entries, random_seed=self.random_seed
        )
        self.assertTrue(os.path.exists(db_path))
        self.verify_db_content(num_entries)
    def test_case_4(self):
        # Test handling invalid num_entries
        with self.assertRaises(Exception):
            task_func(self.db_path, self.table_name, -1, random_seed=self.random_seed)
        with self.assertRaises(Exception):
            task_func(self.db_path, self.table_name, "1", random_seed=self.random_seed)
    def test_case_5(self):
        # Test invalid table names (SQL keywords)
        with self.assertRaises(sqlite3.OperationalError):
            task_func(self.db_path, "Select", 10)
    def test_case_6(self):
        # Test against SQL injection in table_name parameter
        malicious_name = "Test; DROP TABLE IntegrityCheck;"
        with self.assertRaises(sqlite3.OperationalError):
            task_func(self.db_path, malicious_name, 1)
    def verify_db_content(self, num_entries):
        # Connect to the database and check if the table has correct number of entries
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = cur.fetchone()[0]
        self.assertEqual(count, num_entries)
        # Verify data integrity
        cur.execute(f"SELECT name, age, height FROM {self.table_name}")
        rows = cur.fetchall()
        for row in rows:
            self.assertIn(row[0], ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"])
            self.assertIn(row[1], list(range(18, 65)))
            self.assertIn(row[2], list(range(150, 200)))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)