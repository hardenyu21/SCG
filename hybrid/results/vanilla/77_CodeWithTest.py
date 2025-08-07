import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse

def task_func(data):
    try:
        # Check for missing keys
        if 'username' not in data or 'password' not in data:
            raise KeyError("Missing 'username' or 'password' key in input data.")
        
        username = data['username']
        password_base64 = data['password']
        
        # Decode the base64-encoded password
        try:
            password_hash = base64.b64decode(password_base64)
        except (binascii.Error, UnicodeDecodeError):
            raise ValueError("Invalid base64-encoded password.")
        
        # Predefined values for demonstration
        predefined_username = 'admin'
        predefined_password_hash = hashlib.sha256('password'.encode()).digest()
        
        # Authenticate
        if username == predefined_username and password_hash == predefined_password_hash:
            return HttpResponse('Login successful.', status=400)
        else:
            return HttpResponse('Login failed.', status=401)
    
    except (KeyError, UnicodeDecodeError, binascii.Error, ValueError) as e:
        return HttpResponseBadRequest('Bad Request.')

# Example usage:
# data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}
# response = task_func(data)
# print(response.status_code, response.content.decode())
import unittest
from unittest.mock import patch
from django.http import HttpResponseBadRequest, HttpResponse
from django.conf import settings
if not settings.configured:
    settings.configure()
class TestCases(unittest.TestCase):
    @patch('base64.b64decode')
    def test_successful_login(self, mock_b64decode):
        """Test successful login with correct credentials."""
        mock_b64decode.return_value = b'password'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful.', response.content.decode())
    @patch('base64.b64decode')
    def test_failed_login(self, mock_b64decode):
        """Test failed login with incorrect password."""
        mock_b64decode.return_value = b'wrongpassword'
        data = {'username': 'admin', 'password': 'valid_base64'}
        response = task_func(data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Login failed.', response.content.decode())
    def test_invalid_data_structure(self):
        """Test response with missing username or password."""
        data = {'username': 'admin'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    @patch('base64.b64decode', side_effect=ValueError)
    def test_malformed_data(self, mock_b64decode):
        """Test response with non-base64 encoded password."""
        data = {'username': 'admin', 'password': 'not_base64'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
    def test_empty_data(self):
        """Test response when provided with an empty dictionary."""
        data = {}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertIn('Bad Request', response.content.decode())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)