from django.http import HttpResponse
from django.conf import settings
import random
import time
import json

def task_func(data, min_delay, max_delay):
    # Simulate network latency with a random delay
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
    
    # Convert data to JSON
    json_data = json.dumps(data)
    
    # Return an HttpResponse with JSON content
    return HttpResponse(json_data, content_type='application/json')
import unittest
import json
import random
if not settings.configured:
    settings.configure(DEBUG=True)
class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(0)
        data = json.dumps({"key": "value"})
        response = task_func(data, 1, 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"key": "value"})
    def test_case_2(self):
        random.seed(0)
        data = json.dumps({"test": "data", "sample": "value"})
        response = task_func(data, 0, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"test": "data", "sample": "value"})
    def test_case_3(self):
        random.seed(0)
        data = json.dumps({"hello": "world"})
        response = task_func(data, 1, 3)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"hello": "world"})
    def test_case_4(self):
        random.seed(0)
        data = json.dumps({})
        response = task_func(data, 0, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {})
    def test_case_5(self):
        random.seed(0)
        data = json.dumps({"a": 1, "b": 2, "c": 3})
        response = task_func(data, 2, 4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {"a": 1, "b": 2, "c": 3})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)