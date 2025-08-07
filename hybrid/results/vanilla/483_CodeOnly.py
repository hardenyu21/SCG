import re
import pandas as pd

def task_func(df: pd.DataFrame, column_name: str, pattern: str) -> pd.DataFrame:
    # Helper function to reverse words matching the pattern
    def reverse_matching_words(text: str, pattern: str) -> str:
        # Split the text into words
        words = text.split()
        
        # Function to check if a word matches the pattern
        def matches_pattern(word: str) -> bool:
            return re.match(pattern, word) is not None
        
        # Separate words into matching and non-matching
        matching_words = [word for word in words if matches_pattern(word)]
        non_matching_words = [word for word in words if not matches_pattern(word)]
        
        # Reverse the order of matching words
        matching_words.reverse()
        
        # Merge the words back together, maintaining original order for non-matching
        result = []
        matching_index = 0
        for word in words:
            if matches_pattern(word):
                result.append(matching_words[matching_index])
                matching_index += 1
            else:
                result.append(word)
        
        return ' '.join(result)
    
    # If the pattern is empty, return the original DataFrame
    if not pattern:
        return df.copy()
    
    # Apply the helper function to the specified column
    df_copy = df.copy()
    df_copy[column_name] = df_copy[column_name].apply(lambda x: reverse_matching_words(x, pattern))
    
    return df_copy