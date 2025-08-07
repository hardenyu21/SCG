import socket
import ssl
import http.client

def task_func(SERVER_NAME, SERVER_PORT, path):
    # Create a socket object
    context = ssl.create_default_context()
    
    try:
        # Create a secure socket connection
        with socket.create_connection((SERVER_NAME, SERVER_PORT)) as sock:
            with context.wrap_socket(sock, server_hostname=SERVER_NAME) as ssock:
                # Create an HTTP connection object
                connection = http.client.HTTPSConnection(host=SERVER_NAME, port=SERVER_PORT, sock=ssock)
                
                # Make a GET request
                connection.request("GET", path)
                
                # Get the response
                response = connection.getresponse()
                
                # Read the response body
                response_body = response.read().decode('utf-8')
                
                # Close the connection
                connection.close()
                
                return response_body
    
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL handshake error: {e}")
import unittest
from unittest.mock import patch
import http.client
import ssl
import socket
class TestCases(unittest.TestCase):
    @patch('http.client.HTTPSConnection')
    def test_return_type(self, mock_conn):
        """ Test that the function returns a string. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Server Response'
        result = task_func('www.example.com', 443, '/test/path')
        self.assertIsInstance(result, str)
    @patch('http.client.HTTPSConnection')
    def test_different_paths(self, mock_conn):
        """ Test the function with different request paths. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Server Response'
        result = task_func('www.example.com', 443, '/another/path')
        self.assertIsInstance(result, str)
    @patch('http.client.HTTPSConnection')
    def test_connection_error_handling(self, mock_conn):
        """ Test handling of connection errors. """
        mock_conn.side_effect = http.client.HTTPException('Connection error')
        with self.assertRaises(http.client.HTTPException):
            task_func('www.example.com', 443, '/error/path')
    @patch('http.client.HTTPSConnection')
    def test_response_content(self, mock_conn):
        """ Test the content of the response. """
        mock_conn.return_value.getresponse.return_value.read.return_value = b'Expected Content'
        result = task_func('www.example.com', 443, '/content/path')
        self.assertEqual(result, 'Expected Content')
    @patch('socket.create_connection')
    @patch('http.client.HTTPSConnection')
    def test_ssl_handshake_error_handling(self, mock_conn, mock_socket):
        """ Test handling of SSL handshake errors. """
        mock_socket.side_effect = ssl.SSLError('SSL handshake failed')
        with self.assertRaises(ssl.SSLError):
            task_func('badssl.com', 443, '/test/path')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)