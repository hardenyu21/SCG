import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    # Check if the provided API URL is a string
    if not isinstance(api_url, str):
        raise TypeError("The API URL must be a string.")
    
    try:
        # Fetch data from the specified API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Process the JSON response
        data = response.json()
        
        # Convert the JSON data into a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Check if the DataFrame is empty
        if df.empty:
            print("No data to plot.")
            return df, None
        
        # Plot the data using matplotlib
        ax = df.plot()
        plt.title('API Data Plot')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.show()
        
        return df, ax
    
    except requests.exceptions.HTTPError as http_err:
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# Example usage:
# df, ax = task_func("https://api.example.com/data")
import unittest
from unittest.mock import patch, Mock
import pandas as pd
import matplotlib.pyplot as plt
API_URL = "https://api.example.com/data"
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    @patch("requests.get")
    def test_successful_api_call_with_data(self, mock_get):
        """Test the function with a successful API call returning non-empty data."""
        mock_get.return_value = Mock(status_code=200, json=lambda: [{"a": 1, "b": 2}])
        df, plot = task_func("http://example.com/api")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(plot, plt.Axes)
    @patch("requests.get")
    def test_successful_api_call_with_empty_data(self, mock_get):
        """Test the function with a successful API call returning empty data."""
        mock_get.return_value = Mock(status_code=200, json=lambda: [])
        df, plot = task_func("http://example.com/api")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)
        self.assertIsNone(plot)
    @patch("requests.get")
    def test_api_call_with_invalid_json(self, mock_get):
        """Test the function with an API call returning invalid JSON."""
        mock_get.return_value = Mock(
            status_code=200, json=lambda: Exception("Invalid JSON")
        )
        with self.assertRaises(Exception):
            task_func("http://example.com/api")
    @patch("requests.get")
    def test_api_call_with_http_error(self, mock_get):
        """Test the function with an API call that raises an HTTP error."""
        mock_get.side_effect = requests.HTTPError()
        with self.assertRaises(requests.HTTPError):
            task_func("http://example.com/api")
    def test_incorrect_url_type(self):
        """Test the function with an incorrect type for the URL."""
        with self.assertRaises(TypeError):
            task_func(123)
    def tearDown(self):
        plt.close()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)