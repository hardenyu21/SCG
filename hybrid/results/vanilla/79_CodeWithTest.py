import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings

def task_func(request, file_paths):
    # Create an in-memory bytes buffer to hold the ZIP file
    buffer = io.BytesIO()
    
    # Create a ZIP file in the buffer
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            # Ensure the file path is secure and within the allowed directory
            if not file_path.startswith(settings.MEDIA_ROOT):
                raise ValueError("File path is not within the allowed directory.")
            
            # Add the file to the ZIP archive
            zipf.write(file_path, arcname=file_path[len(settings.MEDIA_ROOT):])
    
    # Seek to the beginning of the buffer
    buffer.seek(0)
    
    # Create a FileResponse with the ZIP file as an attachment
    response = FileResponse(buffer, as_attachment=True, filename='files.zip')
    
    return response
import unittest
from unittest.mock import MagicMock, patch
from django.http import HttpRequest, FileResponse
if not settings.configured:
    settings.configure()
class TestCases(unittest.TestCase):
    def setUp(self):
        self.request = HttpRequest()
        self.file_paths = ['file1.gz', 'file2.gz']  # Example file paths for testing
    def test_response_type(self):
        """Ensure the response is an instance of FileResponse."""
        response = task_func(self.request, self.file_paths)
        self.assertIsInstance(response, FileResponse)
    def test_response_status_code(self):
        """Response should have a status code of 200."""
        response = task_func(self.request, self.file_paths)
        self.assertEqual(response.status_code, 200)
    def test_content_type(self):
        """Content type of the response should be set to 'application/zip'."""
        response = task_func(self.request, self.file_paths)
        self.assertEqual(response['Content-Type'], 'application/zip')
    def test_attachment_filename(self):
        """The Content-Disposition should correctly specify the attachment filename."""
        response = task_func(self.request, self.file_paths)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="files.zip"')
    @patch('zipfile.ZipFile')
    def test_zip_file_content(self, mock_zip_file):
        """Zip file should contain the specified files with correct content."""
        mock_zip = MagicMock()
        mock_zip_file.return_value.__enter__.return_value = mock_zip
        task_func(self.request, self.file_paths)
        mock_zip.writestr.assert_any_call('file1.gz', 'This is the content of file1.gz.')
        mock_zip.writestr.assert_any_call('file2.gz', 'This is the content of file2.gz.')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)