from django.http import HttpResponse
import json
import uuid

def task_func(data):
    # Convert the data to JSON format
    json_data = json.dumps(data)
    
    # Generate a UUID for tracking the request
    request_uuid = uuid.uuid4()
    
    # Create an HttpResponse with the JSON data
    response = HttpResponse(json_data, content_type='application/json')
    
    # Add the UUID to the response headers
    response['X-Request-UUID'] = str(request_uuid)
    
    return response