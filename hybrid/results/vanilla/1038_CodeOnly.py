from datetime import datetime
import json
SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024

def task_func(client_socket):
    # Get the current server time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a greeting message
    greeting = "Hello! Welcome to our server."
    
    # Create a JSON-formatted message
    response = {
        "server_time": current_time,
        "greeting": greeting
    }
    
    # Convert the dictionary to a JSON string
    json_response = json.dumps(response)
    
    # Send the JSON response to the client
    client_socket.sendall(json_response.encode('utf-8'))
    
    # Close the client socket
    client_socket.close()