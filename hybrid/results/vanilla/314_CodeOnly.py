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