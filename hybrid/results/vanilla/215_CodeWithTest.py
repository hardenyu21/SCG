import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
HEADERS = {
    'accept': 'application/json'
}

def task_func(url, parameters):
    try:
        # Validate URL
        if not url:
            raise Exception("The URL is invalid or empty.")
        
        # Make the API request
        response = requests.get(url, headers=HEADERS, params=parameters)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to access the URL. Status code: {response.status_code}")
        
        # Parse the response data
        data = response.json()
        
        # Validate data
        if not data:
            raise Exception("Empty data received from the API.")
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Check for numerical columns
        numerical_df = df.select_dtypes(include=['number'])
        
        if numerical_df.empty:
            raise Exception("No numerical data found in the response.")
        
        # Calculate the correlation matrix
        corr_matrix = numerical_df.corr()
        
        # Plot the heatmap
        plt.figure(figsize=(10, 8))
        ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.show()
        
        return df, ax
    
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage:
# df, ax = task_func('https://api.example.com/data', {'param1': 'value1', 'param2': 'value2'})
# Importing the refined function from the refined_function.py file
import unittest
from unittest.mock import patch, Mock
import json
import requests
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_valid_request(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        MOCK_TEXT = '{"data": [1, 2, 3], "data_2": [4, 5, 6]}'
        mock_response.text = MOCK_TEXT
        mock_response.json = lambda: json.loads(MOCK_TEXT)
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        params = {'param1': 'value1'}
        df, ax = task_func(url, params)
        self.assertIsNotNone(df)
        self.assertIsNotNone(ax)
        # Check the content of the DataFrame
        self.assertTrue(df.equals(pd.DataFrame({"data": [1, 2, 3], "data_2": [4, 5, 6]})))
        # Check the correlation matrix
        corr_matrix = df.corr()
        # Check the data plotted on the heatmap
        for i in range(df.shape[1]):
            for j in range(df.shape[1]):
                self.assertEqual(ax.texts[i * df.shape[1] + j].get_text(), str(int(corr_matrix.iloc[i, j])))
    @patch('requests.get')
    def test_empty_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        MOCK_TEXT = '{}'
        mock_response.text = MOCK_TEXT
        mock_response.json = lambda: json.loads(MOCK_TEXT)
        mock_get.return_value = mock_response
        url = 'https://api.example.com/empty_data'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        url = 'https://api.invalid.com/data'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_invalid_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        MOCK_TEXT = 'Invalid JSON'
        mock_response.text = MOCK_TEXT
        mock_response.json = lambda: json.loads(MOCK_TEXT)
        mock_get.return_value = mock_response
        url = 'https://api.example.com/invalid_json'
        params = {'param1': 'value1'}
        with self.assertRaises(Exception):
            task_func(url, params)
    @patch('requests.get')
    def test_valid_request_with_no_params(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        MOCK_TEXT = '{"data": [1, 2, 3, 4, 5]}'
        mock_response.text = MOCK_TEXT
        mock_response.json = lambda: json.loads(MOCK_TEXT)
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        df, ax = task_func(url, {})
        self.assertIsNotNone(df)
        self.assertIsNotNone(ax)
    @patch('requests.get')
    def test_plot_attributes(self, mock_get):
        # Test attributes of the plot
        mock_response = Mock()
        mock_response.status_code = 200
        MOCK_TEXT = '{"id": [1, 2, 3, 4, 5], "user": [6, 7, 8, 9, 10]}'
        mock_response.text = MOCK_TEXT
        mock_response.json = lambda: json.loads(MOCK_TEXT)
        mock_get.return_value = mock_response
        url = 'https://api.example.com/data'
        params = {'param1': 'value1'}
        df, ax = task_func(url, params)
        self.assertTrue(hasattr(ax, 'get_xlabel'))
        self.assertTrue(hasattr(ax, 'get_ylabel'))
        self.assertTrue(hasattr(ax, 'get_title'))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)