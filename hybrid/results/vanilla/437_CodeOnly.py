import pickle
import os
import pandas as pd

def task_func(df, file_name="save.pkl"):
    # Save the DataFrame to a pickle file
    with open(file_name, 'wb') as file:
        pickle.dump(df, file)
    
    # Read the DataFrame back from the pickle file
    with open(file_name, 'rb') as file:
        loaded_df = pickle.load(file)
    
    # Delete the intermediate pickle file
    os.remove(file_name)
    
    # Return the loaded DataFrame
    return loaded_df