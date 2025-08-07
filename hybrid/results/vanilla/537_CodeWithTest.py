import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    try:
        # Load data from the specified table into a DataFrame
        query = f"SELECT age FROM {table_name}"
        df = pd.read_sql_query(query, conn)
        
        # Check for negative age values
        if (df['age'] < 0).any():
            raise ValueError("The data contains negative age values.")
        
        # Plot the age distribution
        plt.figure(figsize=(10, 6))
        ax = sns.histplot(df['age'], bins=30, kde=True)
        ax.set_title('Age Distribution')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        
        # Return the Axes object
        return ax
    
    finally:
        # Close the database connection
        conn.close()
import unittest
import os
import sqlite3
import matplotlib.pyplot as plt
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        # Create test_alt.db with People table
        self.alt_db_path = os.path.join(self.test_dir.name, "test_alt.db")
        conn = sqlite3.connect(self.alt_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE People (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO People VALUES (?, ?)", [("Alice", 25), ("Bob", 30)]
        )
        conn.commit()
        conn.close()
        # Create a standard test.db with Employees table
        self.default_db_path = os.path.join(self.test_dir.name, "test.db")
        conn = sqlite3.connect(self.default_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Employees (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO Employees VALUES (?, ?)", [("Charlie", 35), ("David", 40)]
        )
        conn.commit()
        conn.close()
        # Create standard db with more examples
        self.multiple_db_path = os.path.join(self.test_dir.name, "test_multiple.db")
        conn = sqlite3.connect(self.multiple_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE MultipleAge (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO MultipleAge VALUES (?, ?)",
            [("Alice", 25), ("Bob", 30), ("Charlie", 35)],
        )
        conn.commit()
        conn.close()
        # Create a db for testing edge cases - negative age
        self.negative_age_db_path = os.path.join(
            self.test_dir.name, "test_negative_age.db"
        )
        conn = sqlite3.connect(self.negative_age_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE NegativeAge (name TEXT, age INT)")
        cursor.executemany(
            "INSERT INTO NegativeAge VALUES (?, ?)", [("Eve", -1), ("Frank", 20)]
        )
        conn.commit()
        conn.close()
        # Create a db for testing edge cases - empty
        self.empty_db_path = os.path.join(self.test_dir.name, "test_empty.db")
        conn = sqlite3.connect(self.empty_db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE EmptyAge (name TEXT, age INT)")
        conn.commit()
        conn.close()
    def tearDown(self):
        self.test_dir.cleanup()
        plt.close("all")
    def _check_plot(self, ax, contains_data=True):
        self.assertTrue(isinstance(ax, plt.Axes), "The plot should be an Axes object.")
        self.assertEqual(ax.get_xlabel(), "age", "The x-axis label should be 'age'.")
        if contains_data:
            self.assertTrue(len(ax.lines) > 0, "The plot should contain a KDE line.")
    def test_case_1(self):
        ax = task_func(db_name=self.default_db_path, table_name="Employees")
        self._check_plot(ax)
    def test_case_2(self):
        ax = task_func(db_name=self.alt_db_path)
        self._check_plot(ax)
    def test_case_3(self):
        ax = task_func(db_name=self.default_db_path, table_name="Employees")
        self._check_plot(ax)
    def test_case_4(self):
        ax = task_func(db_name=self.multiple_db_path, table_name="MultipleAge")
        self._check_plot(ax)
    def test_case_5(self):
        ax = task_func(db_name=self.empty_db_path, table_name="EmptyAge")
        self._check_plot(ax, False)
    def test_case_6(self):
        # Test for non-existent table
        with self.assertRaises(Exception):
            task_func(db_name=self.default_db_path, table_name="Nonexistent")
    def test_case_7(self):
        # Test for negative age values
        with self.assertRaises(ValueError):
            task_func(db_name=self.negative_age_db_path, table_name="NegativeAge")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)