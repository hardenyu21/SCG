import sqlite3
import numpy as np
from random import choice, seed

def task_func(db_path, table_name, num_entries, random_seed=None):
    # Constants
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)
    
    # Validate num_entries
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative.")
    
    # Set random seed if provided
    if random_seed is not None:
        seed(random_seed)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            height INTEGER NOT NULL
        )
    ''')
    
    # Insert random data
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cursor.execute(f'''
            INSERT INTO {table_name} (name, age, height)
            VALUES (?, ?, ?)
        ''', (name, age, height))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    # Return the number of rows inserted
    return num_entries
import unittest
import os
import sqlite3
import tempfile
class TestCases(unittest.TestCase):
    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)
    def setUp(self):
        # Setup a temporary directory before each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")
    def tearDown(self):
        # Clean up the temporary directory after each test
        self.temp_dir.cleanup()
    def test_case_1(self):
        # Test inserting 50 entries with a fixed seed
        result = task_func(self.db_path, "SamplePeople", 50, random_seed=42)
        self.assertEqual(result, 50)
    def test_case_2(self):
        # Test inserting 30 entries into a new table with a fixed seed
        result = task_func(self.db_path, "NewPeople", 30, random_seed=42)
        self.assertEqual(result, 30)
    def test_case_3(self):
        # Test inserting 20 entries, verifying smaller batch works as expected
        result = task_func(self.db_path, "SamplePeople", 20, random_seed=42)
        self.assertEqual(result, 20)
    def test_case_4(self):
        # Test inserting a large number of entries (200) with a fixed seed
        result = task_func(self.db_path, "SamplePeople", 200, random_seed=42)
        self.assertEqual(result, 200)
    def test_case_5(self):
        # Test inserting 0 entries to check handling of empty input
        result = task_func(self.db_path, "SamplePeople", 0, random_seed=42)
        self.assertEqual(result, 0)
    def test_case_6(self):
        # Test the content of the rows for correctness against expected values
        task_func(self.db_path, "ContentCheck", 10, random_seed=42)
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM ContentCheck")
        rows = cur.fetchall()
        for row in rows:
            self.assertIn(row[0], self.NAMES)
            self.assertIn(row[1], self.AGES)
            self.assertIn(row[2], self.HEIGHTS)
    def test_case_7(self):
        # Test invalid db path
        with self.assertRaises(sqlite3.OperationalError):
            task_func("/invalid/path.db", "TestTable", 10)
    def test_case_8(self):
        # Test invalid table names (SQL keywords)
        with self.assertRaises(sqlite3.OperationalError):
            task_func(self.db_path, "Select", 10)
    def test_case_9(self):
        # Test handling invalid num_entries
        with self.assertRaises(Exception):
            task_func(self.db_path, "TestTable", -1)
        with self.assertRaises(TypeError):
            task_func(self.db_path, "TestTable", "ten")
    def test_case_10(self):
        # Test handling invalid random seed
        with self.assertRaises(Exception):
            task_func(self.db_path, "TestTable", 10, random_seed="invalid")
    def test_case_11(self):
        # Test different schema in existing table
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE TestTable (id INTEGER)")
        conn.close()
        with self.assertRaises(sqlite3.OperationalError):
            task_func(self.db_path, "TestTable", 10)
    def test_case_12(self):
        # Insert a known set of data and verify its integrity
        task_func(self.db_path, "IntegrityCheck", 1, random_seed=42)
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM IntegrityCheck")
        row = cur.fetchone()
        self.assertIsNotNone(row)
    def test_case_13(self):
        # Test against SQL injection in table_name parameter
        malicious_name = "Test; DROP TABLE IntegrityCheck;"
        with self.assertRaises(sqlite3.OperationalError):
            task_func(self.db_path, malicious_name, 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)