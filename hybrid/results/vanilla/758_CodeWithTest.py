import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
              ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):
    # Check if num_samples is an integer
    if not isinstance(num_samples, int):
        raise ValueError("num_samples must be an integer.")
    
    # Initialize the random number generator
    rng = np.random.default_rng(seed=rng_seed)
    
    # Sample countries
    sampled_countries = rng.choice(countries, size=num_samples)
    
    # Sample ages
    sampled_ages = rng.choice(ages, size=num_samples)
    
    # Encode genders
    label_encoder = LabelEncoder()
    label_encoder.fit(genders)
    encoded_genders = label_encoder.transform(rng.choice(genders, size=num_samples))
    
    # Create a DataFrame
    demographics = pd.DataFrame({
        'Country': sampled_countries,
        'Age': sampled_ages,
        'Gender': encoded_genders
    })
    
    return demographics

# Example usage
demographics = task_func(5, countries=['Austria', 'Germany'], rng_seed=3)
print(demographics)
import unittest
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_num_samples(self):
        'num_samples not an integer'
        self.assertRaises(Exception, task_func, 'test')
    
    # Test Case 1: Basic test with default parameters
    def test_case_1(self):
        demographics = task_func(10, rng_seed=1)
        self.assertEqual(len(demographics), 10)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Russia', 'China', 'USA', 'India', 'Brazil']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 2: Test with custom countries list
    def test_case_2(self):
        demographics = task_func(5, countries=['Canada', 'Australia'], rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Canada', 'Australia']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 3: Test with custom age range
    def test_case_3(self):
        demographics = task_func(5, ages=np.arange(25, 40), rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(all(25 <= age <= 40 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    # Test Case 4: Test with custom gender list
    def test_case_4(self):
        demographics = task_func(5, genders=['Non-Binary'], rng_seed=1)
        self.assertEqual(len(demographics), 5)
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0]))
    # Test Case 5: Test with larger sample size
    def test_case_5(self):
        demographics = task_func(100, rng_seed=1)
        self.assertEqual(len(demographics), 100)
        self.assertTrue(set(demographics['Country'].unique()).issubset(['Russia', 'China', 'USA', 'India', 'Brazil']))
        self.assertTrue(all(18 <= age <= 59 for age in demographics['Age']))
        self.assertTrue(set(demographics['Gender'].unique()).issubset([0, 1]))
    def test_case_6(self):
        'check for specific return value'
        demographics = task_func(5, rng_seed=3)
        expected_df = pd.DataFrame({
            'Country': ['Brazil', 'Russia', 'Russia', 'China', 'Russia'],
            'Age': [51, 54, 42, 19, 21],
            'Gender': [1, 1, 0, 1, 1]
        })
        pd.testing.assert_frame_equal(demographics, expected_df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)