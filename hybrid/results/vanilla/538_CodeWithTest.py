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
import unittest
import sqlite3
import os
import matplotlib.pyplot as plt
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_db_path = os.path.join(self.temp_dir.name, "test.db")
        self.another_test_db_path = os.path.join(self.temp_dir.name, "another_test.db")
        self.nonexistent_db_path = os.path.join(self.temp_dir.name, "nonexistent.db")
        # Setup for 'test.db'
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, height REAL)"
            )
            self.data = [
                ("Alice", 25, 5.5),
                ("Bob", 30, 6.0),
                ("Charlie", 35, 5.8),
                ("David", 40, 6.2),
                ("Eve", 45, 5.9),
                ("Frank", 50, 5.6),
            ]
            cur.executemany(
                "INSERT INTO People (name, age, height) VALUES (?, ?, ?)", self.data
            )
        # Setup for 'another_test.db'
        with sqlite3.connect(self.another_test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE Animals (id INTEGER PRIMARY KEY, name TEXT, lifespan INTEGER, weight REAL)"
            )
            animal_data = [
                ("Dog", 13, 30.0),
                ("Cat", 15, 4.5),
                ("Elephant", 70, 6000.0),
                ("Dolphin", 20, 150.0),
            ]
            cur.executemany(
                "INSERT INTO Animals (name, lifespan, weight) VALUES (?, ?, ?)",
                animal_data,
            )
    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        # Test basic functionality
        ax = task_func(self.test_db_path, "People")
        self.assertEqual(ax.get_xlabel(), "age")
        self.assertEqual(ax.get_ylabel(), "height")
        self.assertEqual(len(ax.collections[0].get_offsets()), 6)
    def test_case_2(self):
        # Test handling non-existent table
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "NonExistentTable")
    def test_case_3(self):
        # Test handling non-existent db
        with self.assertRaises(Exception):
            task_func(self.nonexistent_db_path, "People")
    def test_case_4(self):
        # Table with removed numerical column should raise error
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                f"CREATE TABLE temp AS SELECT id, name, age FROM People WHERE name IN ('Alice', 'Bob')"
            )
            cur.execute(f"DROP TABLE People")
            cur.execute(f"ALTER TABLE temp RENAME TO People")
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "People")
        # Revert changes
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE temp AS SELECT * FROM People")
            cur.execute(f"DROP TABLE People")
            cur.execute(
                f"CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, height REAL)"
            )
            cur.executemany(
                f"INSERT INTO People (name, age, height) VALUES (?, ?, ?)", self.data
            )
    def test_case_5(self):
        # Test another set of data/db
        ax = task_func(self.another_test_db_path, "Animals")
        self.assertEqual(ax.get_xlabel(), "lifespan")
        self.assertEqual(ax.get_ylabel(), "weight")
        self.assertEqual(len(ax.collections[0].get_offsets()), 4)
    def test_case_6(self):
        # Test handling of a table with only one numerical column
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE SingleNumCol (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
            )
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "SingleNumCol")
    def test_case_7(self):
        # Test handling of a table with no numerical columns
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE NoNumCols (id INTEGER PRIMARY KEY, name TEXT, description TEXT)"
            )
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "NoNumCols")
    def test_case_8(self):
        # Test a table where 'id' is the only numerical column
        with sqlite3.connect(self.test_db_path) as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE OnlyIDNum (id INTEGER PRIMARY KEY, name TEXT)")
        with self.assertRaises(Exception):
            task_func(self.test_db_path, "OnlyIDNum")
    def test_case_9(self):
        # Test plotting when the first two numerical columns are not 'id', 'age', or 'height'
        with sqlite3.connect(self.another_test_db_path) as conn:
            cur = conn.cursor()
            custom_data = [("Lion", 15, 190.5), ("Tiger", 20, 220.0)]
            cur.executemany(
                "INSERT INTO Animals (name, lifespan, weight) VALUES (?, ?, ?)",
                custom_data,
            )
        ax = task_func(self.another_test_db_path, "Animals")
        self.assertEqual(ax.get_xlabel(), "lifespan")
        self.assertEqual(ax.get_ylabel(), "weight")
        self.assertGreaterEqual(len(ax.collections[0].get_offsets()), 2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)