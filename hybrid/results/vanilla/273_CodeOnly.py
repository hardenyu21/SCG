import cgi
import http.server
import json

SUCCESS_RESPONSE = {
    'status': 'success',
    'message': 'Data received successfully.'
}

ERROR_RESPONSE = {
    'status': 'error',
    'message': 'Invalid data received.'
}

class POSTRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Check if the content-type is application/json
        content_type = self.headers.get('Content-Type')
        if content_type != 'application/json':
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({
                'status': 'error',
                'message': 'Content-Type header is not application/json'
            })
            self.wfile.write(response.encode('utf-8'))
            return

        # Read the request body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)

        try:
            # Parse the JSON data
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({
                'status': 'error',
                'message': 'Invalid JSON'
            })
            self.wfile.write(response.encode('utf-8'))
            return

        # Check if the 'data' key is present in the JSON object
        if 'data' not in data:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({
                'status': 'error',
                'message': 'No data key in request'
            })
            self.wfile.write(response.encode('utf-8'))
            return

        # If all checks pass, send a 200 OK response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps(SUCCESS_RESPONSE)
        self.wfile.write(response.encode('utf-8'))

def task_func():
    # This function is just a placeholder to indicate where the handler would be used
    # In a real application, you would set up an HTTP server to use this handler
    pass