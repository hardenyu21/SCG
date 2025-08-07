import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    # Create a new browser instance
    br = mechanize.Browser()
    
    # Open the URL
    br.open(url)
    
    # Select the form by its ID
    br.select_form(nr=0)  # Assuming the form is the first one, adjust if needed
    
    # Fill in the form fields with the provided data
    for key, value in data.items():
        br[key] = value
    
    # Submit the form
    response = br.submit()
    
    # Read the response content
    response_content = response.read()
    
    # Parse the response content with BeautifulSoup
    soup = BeautifulSoup(response_content, 'html.parser')
    
    # Extract the title of the page
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    else:
        return 'No Title'

# Example usage:
# url = 'http://example.com'
# form_id = 'exampleForm'
# data = {'field1': 'value1', 'field2': 'value2'}
# print(task_func(url, form_id, data))
import unittest
from unittest.mock import patch, MagicMock
class TestCases(unittest.TestCase):
    @patch('mechanize.Browser')
    def test_return_type(self, mock_browser):
        """ Test that the function returns a string. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Test Page</title></head></html>"
        result = task_func('https://www.example.com/login', 0, {'username': 'admin'})
        self.assertIsInstance(result, str)
    @patch('mechanize.Browser')
    def test_form_submission(self, mock_browser):
        """ Test form submission with mock data. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Successful Submission</title></head></html>"
        result = task_func('https://www.example.com/submit', 0, {'data': 'test'})
        self.assertEqual("Successful Submission", result)
    @patch('mechanize.Browser')
    def test_incorrect_form_id(self, mock_browser):
        """ Test handling of incorrect form ID. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.side_effect = mechanize.FormNotFoundError
        with self.assertRaises(mechanize.FormNotFoundError):
            task_func('https://www.example.com/login', 99, {'username': 'admin'})
    @patch('mechanize.Browser')
    def test_no_title_page(self, mock_browser):
        """ Test handling of pages with no title. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><body><h1>No Title Page</h1></body></html>"
        result = task_func('https://www.example.com/no_title', 0, {})
        self.assertEqual("No Title", result)
    @patch('mechanize.Browser')
    def test_different_data_inputs(self, mock_browser):
        """ Test the function with different data inputs. """
        mock_browser.return_value.open.return_value = MagicMock()
        mock_browser.return_value.select_form.return_value = MagicMock()
        mock_browser.return_value.submit.return_value.read.return_value = "<html><head><title>Different Input</title></head></html>"
        result = task_func('https://www.example.com/different', 0, {'new_field': 'new_value'})
        self.assertIn("Different Input", result)
    @patch('mechanize.Browser')
    def test_invalid_url(self, mock_browser):
        """ Test handling of invalid URL. """
        mock_browser.return_value.open.side_effect = mechanize.URLError(None)
        with self.assertRaises(mechanize.URLError):
            task_func('invalid_url', 0, {'username': 'admin'})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)