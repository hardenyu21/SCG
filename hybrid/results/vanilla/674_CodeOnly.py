import pandas as pd
import os

def task_func(filename):
    # Check if the file exists
    if not os.path.exists(filename):
        return

    # Read the CSV file
    df = pd.read_csv(filename)

    # Reverse the order of the lines, excluding the header
    df_reversed = df.iloc[::-1].reset_index(drop=True)

    # Write the inverted lines back into the file
    df_reversed.to_csv(filename, index=False)

    # Move the cursor back to the beginning of the file
    with open(filename, 'r+') as file:
        file.seek(0)