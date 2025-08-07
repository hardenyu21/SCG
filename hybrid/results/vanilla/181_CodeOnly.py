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