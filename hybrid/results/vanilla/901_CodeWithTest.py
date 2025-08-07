import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def task_func(d):
    if not d:
        return pd.DataFrame()

    # Extract the values for scaling
    data = [[item['x'], item['y'], item['z']] for item in d]
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=['x', 'y', 'z'])
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=['x', 'y', 'z'])
    
    return scaled_df

# Example usage
data = [{'x': -1, 'y': 0, 'z': 5}, {'x': 3, 'y': -15, 'z': 0}, {'x': 0, 'y': 1, 'z': -7}]
print(task_func(data))
import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        result = task_func(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0, 0.5], 'y': [0.642857, 1.0, 0.0], 'z': [0.0, 0.5, 1.0]})
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_case_2(self):
        data = [{'x': -1, 'y': 0, 'z': 5}, {'x': 3, 'y': -15, 'z': 0}, {'x': 0, 'y': 1, 'z': -7}]
        result = task_func(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0, 0.25], 'y': [0.9375, 0.0, 1.0], 'z': [1.0, 0.583333, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)
        
    def test_case_3(self):
        data = []
        result = task_func(data)
        expected_df = pd.DataFrame(columns=['x', 'y', 'z'])
        pd.testing.assert_frame_equal(result, expected_df)
    
    def test_case_4(self):
        data = [{'x': 1}, {'y': 2}, {'z': 3}]
        result = task_func(data)
        expected_df = pd.DataFrame({'x': [0.0, None, None], 'y': [None, 0.0, None], 'z': [None, None, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)
       
    def test_case_5(self):
        data = [{'x': 1, 'y': 2}, {'x': 3, 'z': 4}]
        result = task_func(data)
        expected_df = pd.DataFrame({'x': [0.0, 1.0], 'y': [0.0, None], 'z': [None, 0.0]})
        pd.testing.assert_frame_equal(result, expected_df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)