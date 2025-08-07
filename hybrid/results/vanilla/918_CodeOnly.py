import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    # Define a function to replace acronyms in a single string
    def replace_acronyms(text):
        if pd.isna(text):
            return text
        # Use regex to find acronyms and replace them with full words
        return re.sub(r'\b(' + '|'.join(re.escape(key) for key in mapping.keys()) + r')\b', 
                      lambda match: mapping[match.group(0)], text)
    
    # Apply the replacement function to each element in the DataFrame
    return data.applymap(replace_acronyms)

# Example usage:
# df = pd.DataFrame({
#     'Column1': ['NASA is exploring space.', 'The EU is a union of countries.'],
#     'Column2': ['I love AI.', 'ML is a subset of AI.']
# })
# acronym_mapping = {'NASA': 'National Aeronautics and Space Administration',
#                    'EU': 'European Union',
#                    'AI': 'Artificial Intelligence',
#                    'ML': 'Machine Learning'}
# result_df = task_func(df, acronym_mapping)
# print(result_df)