import numpy as np
import pandas as pd
from scipy import stats

def task_func(input_dict, letter):
    # Convert the input dictionary into a DataFrame
    df = pd.DataFrame(input_dict)
    
    # Filter rows where 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter)]
    
    # Calculate the lengths of these words
    word_lengths = filtered_df['Word'].apply(len)
    
    # Calculate basic statistics: mean, median, and mode
    mean_length = word_lengths.mean()
    median_length = word_lengths.median()
    mode_length = stats.mode(word_lengths)[0][0]  # Get the mode value
    
    # Return the statistics in a dictionary
    return {
        'mean': mean_length,
        'median': median_length,
        'mode': mode_length
    }