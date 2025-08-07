import pandas as pd
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from the Excel file
        logging.info(f"Reading data from Excel file: {excel_file_location}")
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert the DataFrame to a CSV file
        logging.info(f"Converting data to CSV file: {csv_file_location}")
        df.to_csv(csv_file_location, index=False)
        
        # Calculate the sum of each column
        logging.info("Calculating the sum of each column")
        column_sums = df.sum().to_dict()
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: The Excel file does not exist at the specified path: {excel_file_location}")
        raise
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise

# Example usage:
# result = task_func("Sheet1")
# print(result)