import json
import pandas as pd

def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(result)
    
    # Save the DataFrame to a CSV file without the index
    df.to_csv(csv_file_path, index=False)
    
    # Save the list of dictionaries to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)
    
    # The function outputs None
    return None