import pickle
import os

def task_func(filename, data):
    try:
        # Extract the directory from the filename
        directory = os.path.dirname(filename)
        
        # Check if the directory exists, create it if it doesn't
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Serialize the data using pickle and write it to the file
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        
        return True
    except Exception as e:
        # Print the exception for debugging purposes
        print(f"An error occurred: {e}")
        return False