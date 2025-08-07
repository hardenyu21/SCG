import cgi
import http.server
import json

def task_func():
    class POSTRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Check if the Content-Type is application/json
            content_type, _ = cgi.parse_header(self.headers.get('Content-Type'))
            if content_type != 'application/json':
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Content-Type header is not application/json"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Get the content length
            content_length = int(self.headers.get('Content-Length', 0))
            # Read the body of the request
            post_data = self.rfile.read(content_length)

            try:
                # Parse the JSON data
                data = json.loads(post_data)
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Invalid JSON data"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Check if the 'data' key is present
            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "No data received"})
                self.wfile.write(response.encode('utf-8'))
                return

            # If all checks pass, respond with success
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "success", "message": "Data received successfully."})
            self.wfile.write(response.encode('utf-8'))

    return POSTRequestHandler