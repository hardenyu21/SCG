import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    # Check if the input list is empty
    if not list_of_pairs:
        raise Exception("The input array is empty.")
    
    # Extract categories and values from the list of pairs
    categories = []
    values = []
    
    for category, value in list_of_pairs:
        categories.append(category)
        # Check if the value is numeric
        if not isinstance(value, (int, float)):
            raise ValueError("Values are not numeric.")
        values.append(value)
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Normalize the 'Value' column using MinMaxScaler
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        '''test with normal input data'''
        input_data = [('traditional', -4), ('we', 7), ('because', 3), ('ability', 10), ('exactly', -7)]
        result = task_func(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertAlmostEqual(result[result['Category'] == 'traditional']['Value'].item(), 0.176471, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'we']['Value'].item(), 0.823529, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'because']['Value'].item(), 0.588235, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'ability']['Value'].item(), 1.000000, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'exactly']['Value'].item(), 0.000000, places=6)
    def test_case_2(self):
        '''test empty input'''
        input_data = []
        self.assertRaises(Exception, task_func, input_data)
    def test_case_3(self):
        '''non numeric values'''
        input_data = [('fast', 'test'), ('ago', -8), ('player', 7), ('standard', 2), ('specific', 0)]
        self.assertRaises(Exception, task_func, input_data)
    def test_case_4(self):
        '''Floating point values'''
        input_data = [('real', 4.453), ('others', -1.12), ('professor', -2.2), ('other', -5), ('task', -7.933)]
        result = task_func(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertAlmostEqual(result[result['Category'] == 'real']['Value'].item(), 1.000000, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'others']['Value'].item(), 0.550057, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'professor']['Value'].item(), 0.462861, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'other']['Value'].item(), 0.236800, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'task']['Value'].item(), 0.000000, places=6)
    def test_case_5(self):
        '''test for basic output structure'''
        input_data = [('visit', 4), ('brother', -2), ('experience', -10), ('whether', 8), ('hand', 3)]
        result = task_func(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertTrue('Category' in result.columns)
        self.assertTrue(0 <= result['Value'].min() <= 1)
        self.assertTrue(0 <= result['Value'].max() <= 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)