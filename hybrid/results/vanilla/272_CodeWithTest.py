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
import unittest
import requests_mock
import requests
# Constants
SUCCESS_RESPONSE = {
    'status': 'success',
    'message': 'Data received successfully.'
}
ERROR_RESPONSE = {
    'status': 'error',
    'message': 'Invalid data received.'
}
class TestCases(unittest.TestCase):
    @requests_mock.mock()
    def test_invalid_content_type_header(self, m):
        # Mock the POST request to return a 400 status code for invalid content type
        m.post("http://testserver/", status_code=400, json=ERROR_RESPONSE)
        response = requests.post("http://testserver/", headers={"Content-Type": "text/plain"})
        self.assertEqual(response.json(), ERROR_RESPONSE)
        self.assertEqual(response.status_code, 400)
    @requests_mock.mock()
    def test_missing_data_in_request(self, m):
        # Mock the POST request to return a 400 status code for missing 'data' key
        m.post("http://testserver/", status_code=400, json=ERROR_RESPONSE)
        response = requests.post("http://testserver/", json={"wrong_key": "value"})
        self.assertEqual(response.json(), ERROR_RESPONSE)
        self.assertEqual(response.status_code, 400)
    @requests_mock.mock()
    def test_valid_post_request(self, m):
        m.post("http://testserver/", text=json.dumps(SUCCESS_RESPONSE))
        response = requests.post("http://testserver/", json={"data": "value"})
        self.assertEqual(response.json(), SUCCESS_RESPONSE)
        self.assertEqual(response.status_code, 200)
    @requests_mock.mock()
    def test_response_content_type(self, m):
        # Mock the POST request and explicitly set the 'Content-Type' header
        headers = {'Content-Type': 'application/json'}
        m.post("http://testserver/", json=SUCCESS_RESPONSE, headers=headers)
        response = requests.post("http://testserver/", json={"data": "value"})
        self.assertEqual(response.headers["Content-Type"], "application/json")
    @requests_mock.mock()
    def test_incorrect_http_method(self, m):
        m.get("http://testserver/", status_code=405)
        response = requests.get("http://testserver/")
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)