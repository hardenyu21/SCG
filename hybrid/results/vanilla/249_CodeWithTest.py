import pandas as pd
import random
from sklearn.model_selection import train_test_split

def task_func(n_data_points=10000, min_value=0.0, max_value=10.0, test_size=0.2):
    # Generate random floating-point numbers within the specified range
    random_values = [random.uniform(min_value, max_value) for _ in range(n_data_points)]
    
    # Truncate each value to 3 decimal places
    truncated_values = [round(value, 3) for value in random_values]
    
    # Create a DataFrame with the truncated values
    df = pd.DataFrame(truncated_values, columns=['Value'])
    
    # Split the data into train and test sets
    train_set, test_set = train_test_split(df, test_size=test_size, random_state=42)
    
    # Return the train and test sets as a tuple
    return train_set, test_set
import unittest
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        train_data, test_data = task_func()
        self.assertEqual(len(train_data), 8000)  # 80% of 10000
        self.assertEqual(len(test_data), 2000)  # 20% of 10000
    def test_custom_parameters(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=500, min_value=1.0, max_value=5.0, test_size=0.3)
        self.assertEqual(len(train_data), 350)  # 70% of 500
        self.assertEqual(len(test_data), 150)  # 30% of 500
        self.assertTrue(train_data['Value'].between(1.0, 5.0).all())
        self.assertTrue(test_data['Value'].between(1.0, 5.0).all())
    def test_train_test_size_ratio(self):
        random.seed(0)
        n_data_points = 1000
        test_size = 0.25
        train_data, test_data = task_func(n_data_points=n_data_points, test_size=test_size)
        expected_train_size = int(n_data_points * (1 - test_size))
        expected_test_size = n_data_points - expected_train_size
        self.assertEqual(len(train_data), expected_train_size)
        self.assertEqual(len(test_data), expected_test_size)
    def test_value_range(self):
        random.seed(0)
        min_value = 2.0
        max_value = 3.0
        train_data, _ = task_func(min_value=min_value, max_value=max_value)
        self.assertTrue(train_data['Value'].between(min_value, max_value).all())
    def test_value_precision(self):
        random.seed(0)
        train_data, _ = task_func()
        all_three_decimal = all(train_data['Value'].apply(lambda x: len(str(x).split('.')[1]) == 3))
        self.assertFalse(all_three_decimal)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)