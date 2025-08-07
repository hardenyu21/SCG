import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    try:
        # Check if the directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError(f"The directory '{dir}' does not exist.")
        
        # List files in the directory
        files = os.listdir(dir)
        files_list = "\n".join(files)
        
        # Create the email content
        subject = "List of Files in Directory"
        content = f"The following files are in the directory '{dir}':\n\n{files_list}"
        
        # Create the email message
        message = Mail(
            from_email='your-email@example.com',  # Replace with your email
            to_emails=recipient_email,
            subject=subject,
            plain_text_content=content
        )
        
        # Send the email using SendGrid
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        # Check if the email was sent successfully
        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return False
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
        raise HTTPError(http_error)
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception(e)
import unittest
from unittest.mock import patch, MagicMock, Mock
import os
from python_http_client.exceptions import HTTPError
class TestCases(unittest.TestCase):
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_successful_email_send(self, mock_listdir, mock_send, mock_exists):
        """Test successful email sending with a valid directory."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_exists.return_value = True
        mock_send.return_value = MagicMock(status_code=202)
        
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        result = task_func('./valid_directory', api_key, recipient_email)
        self.assertTrue(result)
    def test_invalid_directory(self):
        """Test the handling of an invalid directory."""
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(FileNotFoundError):
            task_func('/nonexistent_directory', api_key, recipient_email)
        
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient.send')
    def test_failed_email_send(self, mock_send, mock_listdir, mock_exists):
        """Test handling of a failed email send by ensuring HTTPError is raised."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_response = Mock(status_code=400, body='Bad Request')
        mock_exists.return_value = True
        mock_send.side_effect = HTTPError(mock_response, 'Failed to send')
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(HTTPError):
            task_func('./valid_directory', api_key, recipient_email)
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_empty_directory(self, mock_listdir, mock_send, mock_exists):
        """Test sending an email with an empty directory."""
        mock_listdir.return_value = []
        mock_send.return_value = MagicMock(status_code=202)
        mock_exists.return_value = True
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        result = task_func('./empty_directory', api_key, recipient_email)
        self.assertTrue(result)
    @patch('os.path.exists')
    @patch('sendgrid.SendGridAPIClient.send')
    @patch('os.listdir')
    def test_generic_exception_handling(self, mock_listdir, mock_send, mock_exists):
        """Test handling of generic exceptions during email sending."""
        mock_listdir.return_value = ['file1.gz', 'file2.gz']
        mock_send.side_effect = Exception('Generic error')
        mock_exists.return_value = True
        api_key = 'test_api_key'
        recipient_email = 'test@example.com'
        with self.assertRaises(Exception):
            task_func('./valid_directory', api_key, recipient_email)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)