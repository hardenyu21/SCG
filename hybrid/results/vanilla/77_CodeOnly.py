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