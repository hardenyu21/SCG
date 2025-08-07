import pandas as pd
import time

def task_func(data_dict, letter):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # Filter rows where the 'Word' column values start with the specified letter
    filtered_df = df[df['Word'].str.startswith(letter, na=False)]
    
    # Calculate the length of each word in the filtered DataFrame
    word_lengths = filtered_df['Word'].apply(len)
    
    # Count the occurrences of each word length
    length_counts = word_lengths.value_counts().to_dict()
    
    return length_counts

# Example usage:
data = {
    'Word': ['apple', 'banana', 'apricot', 'cherry', 'avocado', 'blueberry', 'apex']
}
letter = 'a'
result = task_func(data, letter)
print(result)