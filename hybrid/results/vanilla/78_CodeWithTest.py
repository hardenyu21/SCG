import csv
import io
from django.http import HttpRequest, FileResponse

def task_func(request: HttpRequest, header: list, csv_data: list) -> FileResponse:
    # Create an in-memory text stream
    output = io.StringIO()
    
    # Create a CSV writer object
    writer = csv.writer(output)
    
    # Write the header to the CSV
    writer.writerow(header)
    
    # Write the CSV data
    for row in csv_data:
        writer.writerow(row)
    
    # Seek to the beginning of the stream
    output.seek(0)
    
    # Create a FileResponse object with the CSV data
    response = FileResponse(output, as_attachment=True, filename='data.csv')
    
    return response
import unittest
from unittest.mock import patch
from django.http import HttpRequest, FileResponse
from django.conf import settings
if not settings.configured:
    settings.configure()
class TestCases(unittest.TestCase):
    def setUp(self):
        # Prepare test data
        self.request = HttpRequest()
        self.header = ['id', 'name', 'email']
        self.csv_data = [['1', 'John Doe', 'john@example.com'], ['2', 'Jane Doe', 'jane@example.com']]
    @patch('csv.writer')
    @patch('io.StringIO')
    def test_response_type(self, mock_string_io, mock_csv_writer):
        # Test if the response is of type FileResponse
        response = task_func(self.request, self.header, self.csv_data)
        self.assertIsInstance(response, FileResponse)
    @patch('csv.writer')
    @patch('io.StringIO')
    def test_response_status_code(self, mock_string_io, mock_csv_writer):
        # Test if the response has status code 200
        response = task_func(self.request, self.header, self.csv_data)
        self.assertEqual(response.status_code, 200)
    @patch('csv.writer')
    @patch('io.StringIO')
    def test_content_type(self, mock_string_io, mock_csv_writer):
        # Test if the Content-Type header is set to 'text/csv'
        response = task_func(self.request, self.header, self.csv_data)
        self.assertEqual(response['Content-Type'], 'text/csv')
    @patch('csv.writer')
    @patch('io.StringIO')
    def test_attachment_filename(self, mock_string_io, mock_csv_writer):
        # Test if the Content-Disposition is set correctly for file download
        response = task_func(self.request, self.header, self.csv_data)
        self.assertIn('attachment; filename="data.csv"', response['Content-Disposition'])
    @patch('csv.writer')
    @patch('io.StringIO')
    def test_csv_file_content(self, mock_string_io, mock_csv_writer):
        # Test if csv.writer methods are called to write the header and rows correctly
        response = task_func(self.request, self.header, self.csv_data)
        mock_csv_writer.return_value.writerow.assert_called_with(self.header)
        mock_csv_writer.return_value.writerows.assert_called_with(self.csv_data)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)