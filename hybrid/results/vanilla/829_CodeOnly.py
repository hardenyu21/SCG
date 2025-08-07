import pandas as pd
from statistics import mean

def task_func(df: pd.DataFrame) -> dict:
    # Check if the DataFrame contains the required columns
    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError("The DataFrame must contain 'Name' and 'Score' columns.")
    
    # Group the DataFrame by 'Name' and calculate the average score for each name
    grouped = df.groupby('Name')['Score'].mean().reset_index()
    
    # Create a dictionary of generator objects
    gen_dict = {
        row['Name']: (lambda name=row['Name'], score=row['Score']: ((name, score),))()
        for _, row in grouped.iterrows()
    }
    
    return gen_dict

# Example usage
df_sample = pd.DataFrame({
    'Name': ['Micky', 'Donald', 'Girl'],
    'Score': [25.2, 9, -1]
})

gen_dict = task_func(df_sample)
print({key: next(value) for key, value in gen_dict.items()})