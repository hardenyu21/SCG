import numpy as np
import pandas as pd

def task_func(country_dict):
    # Extract the country names from the dictionary keys
    countries = list(country_dict.keys())
    
    # Generate random GDP values for each country
    gdp_values = np.random.randint(1_000_000_000, 100_000_000_000, size=len(countries))
    
    # Create a DataFrame with countries as the index and GDP values as the column
    df = pd.DataFrame(data=gdp_values, index=countries, columns=['GDP'])
    
    return df

# Example usage:
country_dict = {
    'USA': 'Washington, D.C.',
    'Germany': 'Berlin',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'India': 'New Delhi'
}

df = task_func(country_dict)
print(df)
import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        country_dict = {'John': 'USA', 'Alice': 'UK', 'Bob': 'China'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA', 'UK', 'China'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_2(self):
        country_dict = {'Charlie': 'Japan', 'David': 'Australia'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['Japan', 'Australia'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_3(self):
        country_dict = {'Eve': 'USA', 'Frank': 'UK', 'Grace': 'China', 'Hannah': 'Japan', 'Ian': 'Australia'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA', 'UK', 'China', 'Japan', 'Australia'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_4(self):
        country_dict = {'Jack': 'USA'}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), ['USA'])
        self.assertTrue(result['GDP'].apply(lambda x: 1000000000 <= x <= 100000000000).all())
    def test_case_5(self):
        country_dict = {}
        result = task_func(country_dict)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertListEqual(list(result.index), [])
        self.assertTrue(result.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)