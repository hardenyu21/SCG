import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the dictionary has the required keys
    required_keys = {'Name', 'Age', 'Scores'}
    if not all(key in data for key in required_keys):
        raise ValueError("The dictionary does not have the required keys.")
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by 'Name' and 'Age' in ascending order
    df_sorted = df.sort_values(by=['Name', 'Age'], ascending=[True, True])
    
    # Calculate the average score per student
    df['Average Score'] = df['Scores'].apply(lambda scores: sum(scores) / len(scores) if scores else None)
    average_scores_series = df.set_index('Name')['Average Score']
    
    # Find the most common age
    if df['Age'].empty:
        most_common_age = None
    else:
        age_counts = Counter(df['Age'])
        most_common_age = age_counts.most_common(1)[0][0]
    
    return df_sorted, average_scores_series, most_common_age