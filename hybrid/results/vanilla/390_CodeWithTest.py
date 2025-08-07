import pandas as pd
import requests
from io import StringIO

def task_func(csv_url_dict, sort_by_column="title"):
    # Check if the dictionary is empty or if the "URL" key does not exist
    if not csv_url_dict or "URL" not in csv_url_dict:
        raise ValueError("The dictionary is empty or does not contain the 'URL' key.")
    
    # Fetch the CSV data from the URL
    url = csv_url_dict["URL"]
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    # Read the CSV data into a pandas DataFrame
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    
    # Sort the DataFrame based on the specified column
    if sort_by_column not in df.columns:
        raise ValueError(f"The specified column '{sort_by_column}' does not exist in the DataFrame.")
    
    sorted_df = df.sort_values(by=sort_by_column)
    
    return sorted_df
import unittest
from unittest.mock import patch
from io import StringIO
import pandas as pd
import requests
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_case_1(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func({"URL": "http://example.com/data.csv"}, 'title')
        expected_titles = ["Apple", "Banana", "Cherry"]
        actual_titles = result['title'].tolist()
        self.assertEqual(actual_titles, expected_titles)
    @patch('requests.get')
    def test_case_2(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func({"URL": "http://example.com/tst.csv"}, 'price')
        self.assertEqual(result.iloc[0]['price'], 0.2)
        self.assertEqual(result.iloc[1]['price'], 0.3)
        self.assertEqual(result.iloc[2]['price'], 0.5)
    @patch('requests.get')
    def test_case_3(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        
        
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func({"URL": "http://example.com/tst.csv"})
        self.assertEqual(result.iloc[0]['title'], "Apple")
        self.assertEqual(result.iloc[1]['title'], "Banana")
        self.assertEqual(result.iloc[2]['title'], "Cherry")
    @patch('requests.get')
    def test_case_4(self, mock_get):
        mock_csv_content =  "id,title,price\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func({"URL": "http://example.com/empty.csv"})
        self.assertTrue(result.empty)
    @patch('requests.get')
    def test_case_5(self, mock_get):
        mock_csv_content = "id,name,age\n2,John,25\n1,Alice,30\n3,Bob,20\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func({"URL": "http://example.com/test_2.csv"}, "age")
        self.assertEqual(result.iloc[0]['name'], "Bob")
        self.assertEqual(result.iloc[1]['name'], "John")
        self.assertEqual(result.iloc[2]['name'], "Alice")
    
    @patch('requests.get')
    def test_case_6(self, mock_get):
        mock_csv_content =  "id,title,price\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 400
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        with self.assertRaises(ValueError):
            result = task_func({"link": "http://example.com/error.csv"})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)