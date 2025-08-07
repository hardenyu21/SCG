import pandas as pd
from scipy.stats import chi2_contingency

def task_func(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    # Check if the number of specified columns is 3
    if len(columns) != 3:
        raise ValueError("The number of specified columns must be 3.")
    
    # Check if the specified columns are contained in df
    if not all(col in df.columns for col in columns):
        raise ValueError("The specified columns are not contained in the DataFrame.")
    
    # Unpack the column names
    col1, col2, col3 = columns
    
    # Filter the DataFrame based on the criteria
    filtered_df = df[(df[col2] > larger) & (df[col3] == equal)]
    
    # Check if there's sufficient data for the test
    if filtered_df.empty:
        raise ValueError("There's insufficient data for the test (no rows meeting the criteria).")
    
    # Create a contingency table of the first two columns
    contingency_table = pd.crosstab(filtered_df[col1], filtered_df[col2])
    
    # Perform the chi-square independence test
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    
    # Return the p-value
    return p_value
import unittest
import pandas as pd
import faker
class TestCases(unittest.TestCase):
    def test_column_not_in_df(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'D': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data)
    def test_column_number(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'C': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data, ['A'])
        self.assertRaises(Exception, task_func, data, ['A', 'B', 'C', 'D'])
    def test_no_data_after_filer(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [20 for i in range(rows)],
                'C': [901 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, task_func, data)
    def test_medium_dataframe(self):
        # Test with a medium-sized dataframe (50 rows)
        fake = faker.Faker()
        fake.seed_instance(12)
        rows = 50
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(899, 901) for i in range(rows)] 
            }
        )        
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 0.23, places=1)
    def test_large_dataframe(self):
        # Test with a large dataframe (1000 rows)
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(800, 950) for i in range(rows)] 
            }
        )        
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_very_large_dataframe(self):
        data = pd.DataFrame(
            {
                'A': ['a', 'a', 'a', 'a', 'a'],
                'B': [70, 70, 70, 70, 70],
                'C': [900, 900, 900, 900, 900] 
            }
        )
        p_value = task_func(data)
        self.assertAlmostEqual(p_value, 1.0, places=1)
    def test_huge_dataframe(self):
        # different column names
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(821, 950) for i in range(rows)] 
            }
        )        
        p_value = task_func(data, columns=['test', 'five', '1'])
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_diff_filter(self):
        # different filter values
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(19, 21) for i in range(rows)] 
            }
        )        
        p_value = task_func(data, columns=['test', 'five', '1'], larger=100, equal=20)
        self.assertAlmostEqual(p_value, 0.35, places=1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)