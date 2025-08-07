import json
import urllib.parse
import hmac
import hashlib

def task_func(req_data, secret_key):
    # Check if req_data is a dictionary
    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(req_data, separators=(',', ':'))
    
    # Create a new HMAC object using the secret key and SHA256
    hmac_obj = hmac.new(secret_key.encode('utf-8'), json_data.encode('utf-8'), hashlib.sha256)
    
    # Get the hexadecimal digest of the HMAC
    hmac_digest = hmac_obj.hexdigest()
    
    # URL encode the HMAC digest
    url_encoded_signature = urllib.parse.quote(hmac_digest, safe='')
    
    # Replace spaces with '+'
    final_signature = url_encoded_signature.replace(' ', '+')
    
    return final_signature