import json
import random
import hashlib
from datetime import datetime

def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    # Validate inputs
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object.")
    if not isinstance(salt, str):
        raise ValueError("salt must be a string.")
    
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Generate a random lowercase alphanumeric password
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    # Create the string to hash: password + salt + utc_datetime string representation
    datetime_str = utc_datetime.isoformat()
    hash_input = password + salt + datetime_str
    
    # Hash the input using SHA-256
    hash_object = hashlib.sha256(hash_input.encode())
    hashed_password = hash_object.hexdigest()
    
    # Encode the hashed password as a JSON string
    json_encoded_password = json.dumps(hashed_password)
    
    return json_encoded_password
import re
import pytz
import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input 1
        utc_time = datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time, seed=79)
        
        # Decoding the JSON string
        decoded_str = json.loads(password_json_str)
        
        # Check if the decoded string is a valid SHA-256 hash
        self.assertEqual(len(decoded_str), 64)  # SHA-256 produces a 64 character hash
        self.assertTrue(re.match(r"^[a-f0-9]{64}$", decoded_str))  # Check if it's a valid hexadecimal
        # Check the hashed password
        self.assertEqual(decoded_str, "3da4b6faf766416fe75b2e5efd831f0fc907e0cc450e7fb58f61110be0a6ab3a") # Expected hash
    def test_case_2(self):
        # Input 2
        utc_time = datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time)
        
        # Decoding the JSON string
        decoded_str = json.loads(password_json_str)
        
        # Check if the decoded string is a valid SHA-256 hash
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match(r"^[a-f0-9]{64}$", decoded_str))
    def test_case_3(self):
        # Input 3
        utc_time = datetime(2050, 12, 31, 23, 59, 59, tzinfo=pytz.UTC)
        password_json_str = task_func(utc_time, salt="random salt be like")
        
        # Decoding the JSON string
        decoded_str = json.loads(password_json_str)
        
        # Check if the decoded string is a valid SHA-256 hash
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match(r"^[a-f0-9]{64}$", decoded_str))
        self.assertEqual(decoded_str, "afd33d74be6cbfb08c6ad76d6f8556ef910e252912d7ebb13603ace3edccd260") # Expected hash
    def test_case_4(self):
        # Input 4
        utc_time = datetime(2020, 2, 29, 5, 30, 15, tzinfo=pytz.UTC)  # A leap year date
        password_json_str = task_func(utc_time)
        
        # Decoding the JSON string
        decoded_str = json.loads(password_json_str)
        
        # Check if the decoded string is a valid SHA-256 hash
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match(r"^[a-f0-9]{64}$", decoded_str))
    def test_case_5(self):
        # Input 5
        utc_time = datetime(2000, 1, 1, 12, 0, 0, tzinfo=pytz.UTC)  # A date from the past millennium
        password_json_str = task_func(utc_time)
        
        # Decoding the JSON string
        decoded_str = json.loads(password_json_str)
        
        # Check if the decoded string is a valid SHA-256 hash
        self.assertEqual(len(decoded_str), 64)
        self.assertTrue(re.match(r"^[a-f0-9]{64}$", decoded_str))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)