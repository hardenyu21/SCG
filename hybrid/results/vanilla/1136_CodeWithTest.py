import bs4
import requests
import re
import csv

def task_func(url="http://example.com", csv_path="emails.csv", 
              regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
              headers={'User-Agent': 'Mozilla/5.0'}):
    # Send a GET request to the specified URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    # Parse the webpage content using BeautifulSoup
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the webpage
    text = soup.get_text()
    
    # Find all email addresses using the specified regex pattern
    emails = re.findall(regex, text)
    
    # Write the extracted emails to a CSV file
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Emails'])  # Write the header
        for email in emails:
            writer.writerow([email])
    
    # Return the path to the CSV file
    return csv_path
import unittest
from unittest.mock import patch, ANY
import os
import csv
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to hold any output files
        self.test_dir = tempfile.mkdtemp()
        self.addCleanup(lambda: os.rmdir(self.test_dir))
    def tearDown(self):
        # Clean up all files created during the tests
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
    @patch('requests.get')
    def test_extraction_and_saving_default(self, mock_get):
        """Test extracting emails using default parameters and saving to default path."""
        mocked_html_content = """<html><body>Emails: test1@example.com, test2@domain.com</body></html>"""
        mock_get.return_value.text = mocked_html_content
        
        csv_path = os.path.join(self.test_dir, "emails.csv")
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            task_func(csv_path=csv_path)
            args, kwargs = mocked_file.call_args
            self.assertEqual(args[0], csv_path)  # Assert the first argument is the file path
            try:
                self.assertEqual(kwargs['mode'], 'w')  # Assert the file is opened in write mode
            except:
                self.assertEqual(args[1], 'w')
            self.assertEqual(kwargs['newline'], '')  # Assert newline handling
    @patch('requests.get')
    def test_extraction_custom_url(self, mock_get):
        """Test the email extraction from a custom URL and ensure file creation even if no emails are found."""
        mock_get.return_value.text = "<html><body>No email here</body></html>"
        csv_path = os.path.join(self.test_dir, "output.csv")
        result = task_func(url="http://mocked-url.com", csv_path=csv_path)
        self.assertEqual(result, csv_path)
        self.assertTrue(os.path.exists(csv_path))  # Ensuring file is created
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        self.assertEqual(data, [['Emails']])
    @patch('requests.get')
    def test_extraction_custom_regex(self, mock_get):
        """Test extraction with a custom regex pattern."""
        mocked_html_content = "<html><body>Email: unique@example.com, other@sample.com</body></html>"
        mock_get.return_value.text = mocked_html_content
        csv_path = os.path.join(self.test_dir, "custom_regex.csv")
        task_func(csv_path=csv_path, regex=r"\b[A-Za-z0-9._%+-]+@example.com\b")
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            emails = [row for row in reader]
        self.assertEqual(emails, [['Emails'], ['unique@example.com']])  # Only matching specific domain
    @patch('requests.get')
    def test_with_headers_customization(self, mock_get):
        """Test extraction with customized headers."""
        mock_get.return_value.text = "<html><body>Email: info@test.com</body></html>"
        csv_path = os.path.join(self.test_dir, "headers.csv")
        task_func(csv_path=csv_path, headers={'User-Agent': 'Custom-Agent'})
        self.assertTrue(os.path.exists(csv_path))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)