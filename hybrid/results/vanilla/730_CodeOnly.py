import pickle
import os
from datetime import datetime

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    # Load the datetime object back from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    
    # Return the loaded datetime object
    return loaded_dt

# Example usage:
# dt = datetime.now()
# loaded_dt = task_func(dt)
# print("Original datetime:", dt)
# print("Loaded datetime:", loaded_dt)