import requests
from bs4 import BeautifulSoup

def task_func(url, tag):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the first occurrence of the specified HTML tag
        element = soup.find(tag)
        
        # Return the text content of the tag if found, otherwise return None
        return element.get_text(strip=True) if element else None
    
    except requests.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return None
import unittest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
import os
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_title_tag_found(self, mock_get):
        """Test retrieving the title tag."""
        html_content = "<html><head><title>Test Page</title></head><body></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "title")
        self.assertEqual(result, "Test Page")
    @patch('requests.get')
    def test_h1_tag_found(self, mock_get):
        """Test retrieving the h1 tag."""
        html_content = "<html><body><h1>This is a test page</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "h1")
        self.assertEqual(result, "This is a test page")
    @patch('requests.get')
    def test_nonexistent_tag(self, mock_get):
        """Test for a tag that doesn't exist."""
        html_content = "<html><body><h1>Existing Tag</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "h2")
        self.assertIsNone(result)
    def test_invalid_url_handling(self):
        """Test how the function handles an invalid URL."""
        with self.assertRaises(requests.exceptions.RequestException):
            task_func("invalid_url", "title")
    @patch('requests.get')
    def test_malformed_html(self, mock_get):
        """Test the function with a malformed HTML input."""
        html_content = "<html><head><title>Test Page</title><head><body><h1>This is a test page<h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "title")
        self.assertEqual(result, "Test Page")
        result = task_func("http://test.com", "h1")
        self.assertIsNone(result)
    @patch('requests.get')
    def test_multiple_matching_tags(self, mock_get):
        """Test the function with multiple tags of the same type."""
        html_content = "<html><body><p>First Paragraph</p><p>Second Paragraph</p></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "p")
        self.assertEqual(result, "First Paragraph")
    @patch('requests.get')
    def test_empty_tag(self, mock_get):
        """Test the function with an empty tag content."""
        html_content = "<html><body><div></div><h1>Not empty</h1></body></html>"
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response
        result = task_func("http://test.com", "div")
        self.assertIsNone(result)
        result = task_func("http://test.com", "h1")
        self.assertEqual(result, "Not empty")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)