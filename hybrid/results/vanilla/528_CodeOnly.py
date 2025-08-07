import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    # Check if the file has a .csv extension
    if not file_path.endswith('.csv'):
        raise ValueError("The file must have a .csv extension.")
    
    # Read the CSV file and identify duplicate rows
    duplicate_counter = Counter()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header
        rows = [tuple(row) for row in reader]
        row_counter = Counter(rows)
        for row, count in row_counter.items():
            if count > 1:
                duplicate_counter[row] = count
    
    # Convert duplicate rows into a pandas DataFrame
    duplicate_rows = [(row, count) for row, count in duplicate_counter.items()]
    df = pd.DataFrame(duplicate_rows, columns=['Row', 'Count'])
    
    # Plot the duplicate rows using matplotlib
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Row', y='Count', ax=ax)
    ax.set_title('Duplicate Rows in CSV File')
    ax.set_xlabel('Rows')
    ax.set_ylabel('Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Return the dictionary and the Axes object
    return duplicate_counter, ax

# Example usage:
# duplicate_dict, ax = task_func('your_file.csv')
# plt.show()