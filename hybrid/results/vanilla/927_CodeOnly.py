import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Replace all occurrences of '\n' with '<br>' in the specified column
    if column_name in df.columns:
        df[column_name] = df[column_name].str.replace('\n', '<br>', regex=False)
    
    # Encode the specified column as a categorical variable using LabelEncoder
    label_encoder = LabelEncoder()
    df[column_name] = label_encoder.fit_transform(df[column_name])
    
    return df