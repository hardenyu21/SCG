import json
import random

# Constants
DATA = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Peter', 'age': 35, 'city': 'London'},
    {'name': 'Susan', 'age': 25, 'city': 'Sydney'},
    {'name': 'Alice', 'age': 28, 'city': 'Paris'},
    {'name': 'Bob', 'age': 40, 'city': 'Tokyo'},
    {'name': 'Charlie', 'age': 22, 'city': 'Beijing'},
    {'name': 'David', 'age': 33, 'city': 'Mumbai'},
    {'name': 'Eve', 'age': 27, 'city': 'Berlin'},
    {'name': 'Frank', 'age': 32, 'city': 'Moscow'},
    {'name': 'Grace', 'age': 29, 'city': 'Rome'}
]

def task_func(utc_datetime, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Select a random person from the DATA list
    selected_person = random.choice(DATA)
    
    # Add the UTC timestamp to the selected person's data
    selected_person['timestamp'] = utc_datetime
    
    # Encode the person's data as a JSON string
    json_string = json.dumps(selected_person)
    
    return json_string
import unittest
import pytz
import doctest
from datetime import datetime
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        utc_time = datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2023-06-15T12:00:00+00:00')
        
    def test_case_2(self):
        utc_time = datetime(2022, 5, 10, 10, 30, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2022-05-10T10:30:00+00:00')
        # Test with seed
        self.assertEqual(person_data['name'], 'David')
        self.assertEqual(person_data['age'], 33)
        self.assertEqual(person_data['city'], 'Mumbai')
        
    def test_case_3(self):
        # Test with current UTC time
        utc_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and current timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        
    def test_case_4(self):
        utc_time = datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC)
        person_json_str = task_func(utc_time, seed=101)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2021-01-01T00:00:00+00:00')
        # Test with seed
        self.assertEqual(person_data['name'], 'Grace')
        self.assertEqual(person_data['age'], 29)
        self.assertEqual(person_data['city'], 'Rome')
        
    def test_case_5(self):
        utc_time = datetime(2020, 2, 29, 15, 45, 0, tzinfo=pytz.UTC)  # Leap year date
        person_json_str = task_func(utc_time)
        person_data = json.loads(person_json_str)
        
        # Assert that the returned data has the expected fields and timestamp
        self.assertIn('name', person_data)
        self.assertIn('age', person_data)
        self.assertIn('city', person_data)
        self.assertIn('timestamp', person_data)
        self.assertEqual(person_data['timestamp'], '2020-02-29T15:45:00+00:00')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)