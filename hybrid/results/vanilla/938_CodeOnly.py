import re
import pandas as pd

def task_func(input_df):
    # Define a function to clean the text
    def clean_text(text):
        # Remove all special characters, punctuation marks, and spaces
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text)
        return cleaned

    # Apply the clean_text function to the 'text' column
    input_df['clean_text'] = input_df['text'].apply(clean_text)

    # Calculate the length of the cleaned text
    input_df['text_length'] = input_df['clean_text'].apply(len)

    return input_df