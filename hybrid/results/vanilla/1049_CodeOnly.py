import re
import pandas as pd

def task_func(input_string: str) -> pd.DataFrame:
    # Split the input string into lines
    lines = input_string.splitlines()
    
    # Process each line: replace tabs with spaces and filter out empty lines
    processed_lines = [re.sub(r'\t', ' ', line).strip() for line in lines if line.strip()]
    
    # Create a DataFrame with the processed lines
    df = pd.DataFrame(processed_lines, columns=['Text'])
    
    return df