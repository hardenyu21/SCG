import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Construct the full file path
    file_path = os.path.join(excel_directory, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified Excel file '{file_path}' does not exist.")
    
    # Load the Excel file into a DataFrame
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the Excel file: {e}")
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the DataFrame.")
    
    # Validate and convert start_date and end_date to datetime objects
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("start_date and end_date must be in the format 'YYYY-MM-DD'.")
    
    # Filter the DataFrame based on the date range
    try:
        filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]
    except TypeError:
        raise ValueError(f"The column '{column_name}' does not contain date data that can be filtered.")
    
    return filtered_df