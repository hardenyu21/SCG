import random
import string
from django.http import HttpResponse

def task_func(request, session_expire_time):
    # Generate a random session key of length 20
    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    
    # Check if the session key contains both letters and digits
    if not (any(c.isalpha() for c in session_key) and any(c.isdigit() for c in session_key)):
        raise ValueError("Session key must contain both letters and digits.")
    
    # Check if the session key length is exactly 20
    if len(session_key) != 20:
        raise ValueError("Session key length must be exactly 20 characters.")
    
    # Create an HttpResponse object
    response = HttpResponse("Session key generated successfully.")
    
    # Set the session key in a cookie with the specified expiration time
    response.set_cookie('session_key', session_key, max_age=session_expire_time)
    
    return response
import unittest
from unittest.mock import patch
from django.http import HttpRequest
from django.conf import settings
# Configure Django settings if not already configured
if not settings.configured:
    settings.configure(
        DEFAULT_CHARSET='utf-8',
        SECRET_KEY='a-very-secret-key',
    )
class TestCases(unittest.TestCase):
    @patch('random.choices')
    def test_session_key_in_cookies(self, mock_random_choices):
        """Test if 'session_key' is set in the response cookies with the correct expiration."""
        mock_random_choices.return_value = ['1a'] * 10  # Mock session key as 'aaaaaaaaaaaaaaaaaaaa'
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIn('session_key', response.cookies)
        self.assertEqual(response.cookies['session_key']['max-age'], 60)
    @patch('random.choices')
    def test_session_key_length(self, mock_random_choices):
        """Test if the length of 'session_key' is 20."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertEqual(len(response.cookies['session_key'].value), 20)
    @patch('random.choices')
    def test_response_content(self, mock_random_choices):
        """Test if the response content includes the expected message."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIn('Session key generated successfully.', response.content.decode())
    @patch('random.choices')
    def test_response_type(self, mock_random_choices):
        """Test if the response object is of type HttpResponse."""
        mock_random_choices.return_value = ['1a'] * 10
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertIsInstance(response, HttpResponse)
    @patch('random.choices')
    def test_raise_error(self, mock_random_choices):
        """Test if the function raises ValueError when the session key does not contain both letters and digits."""
        mock_random_choices.return_value = ['a'] * 20  # Only letters, no digits
        request = HttpRequest()
        with self.assertRaises(ValueError):
            task_func(request, 60)  # pass the session_expire_time
    @patch('random.choices')
    def test_valid_session_key(self, mock_random_choices):
        """Test if the function completes without error when session key is valid."""
        # Ensure the mock session key always contains both letters and digits
        mock_random_choices.return_value = list('A1' * 10)  # This creates a string 'A1A1A1A1A1A1A1A1A1A1'
        request = HttpRequest()
        response = task_func(request, 60)  # pass the session_expire_time
        self.assertEqual(len(response.cookies['session_key'].value), 20)
        self.assertTrue(any(char.isalpha() for char in response.cookies['session_key'].value))
        self.assertTrue(any(char.isdigit() for char in response.cookies['session_key'].value))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)