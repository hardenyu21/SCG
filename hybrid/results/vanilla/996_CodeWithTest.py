import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        title = soup.title.string if soup.title else None

        # Prepare the data to be saved in JSON format
        data = {"title": title}

        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Write the JSON data to the file, with each title on a new line
            json.dump(data, file)
            file.write('\n')

        return file_name

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None
import unittest
from unittest.mock import patch, mock_open
import requests
import json
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_scrape_title_page_1(self, mock_file):
        """Test that the title is scraped from a web page and saved to a file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>Test Page 1</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": "Test Page 1"}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_scrape_title_page_2(self, mock_file):
        """Test that the title is scraped from a web page and saved to a file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>Test Page 2</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com", "AnotherOutput.txt")
            self.assertEqual(file_path, "AnotherOutput.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": "Test Page 2"}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_invalid_url(self, mock_file):
        """Test that an exception is raised when the URL is invalid"""
        with self.assertRaises(requests.RequestException):
            task_func("http://invalid-url")
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_page_without_title(self, mock_file):
        """Test that 'None' is saved as the title when the web page does not have a title"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<html><head></head><body></body></html>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": None}) + "\n"
            )
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_very_long_title(self, mock_file):
        """Test that a very long title is saved correctly"""
        long_title = "A" * 1024  # A very long title of 1024 characters
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = f"<title>{long_title}</title>".encode()
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_once_with(
                json.dumps({"title": long_title}) + "\n"
            )
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps({"title": "Existing Title"}) + "\n",
    )
    def test_append_to_existing_file(self, mock_file):
        """Test that data is appended to an existing file"""
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_response._content = b"<title>New Title</title>"
        with patch("requests.get", return_value=mock_response):
            file_path = task_func("http://example.com")
            self.assertEqual(file_path, "Output.txt")
            mock_file().write.assert_called_with(
                json.dumps({"title": "New Title"}) + "\n"
            )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)