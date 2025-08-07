import pandas as pd
import random

def task_func(csv_file, column_name='data', pattern=r'\d+[xX]', sample_size=None, seed=42):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")
    
    # Find rows where the specified column matches the regex pattern
    matches = df[df[column_name].astype(str).str.contains(pattern, regex=True)]
    
    # If sample_size is specified, perform random sampling
    if sample_size is not None:
        if sample_size > len(matches):
            raise ValueError("Sample size cannot be greater than the number of matches.")
        
        # Set the random seed for reproducibility
        random.seed(seed)
        
        # Generate a random sample of indices
        sample_indices = random.sample(range(len(matches)), sample_size)
        
        # Return the sampled DataFrame
        return matches.iloc[sample_indices]
    
    # Return all matches if no sample size is specified
    return matches