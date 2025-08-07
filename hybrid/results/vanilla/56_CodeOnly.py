import pandas as pd
import regex as re

def task_func(text):
    # Define a regex pattern to extract score and category
    pattern = r'Score: (\d+), Category: (\w+)'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Convert matches to a list of dictionaries
    data = [{'Score': int(score), 'Category': category} for score, category in matches]
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    return df