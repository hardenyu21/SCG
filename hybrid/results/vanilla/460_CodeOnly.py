import subprocess
import pandas as pd
import matplotlib.pyplot as plt

def task_func(script_path, output_file_path):
    # Execute the script
    try:
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Script execution failed: {e.stderr}")

    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(output_file_path)
    except Exception as e:
        raise ValueError(f"Failed to read CSV file: {e}")

    # Check if the CSV has exactly two columns
    if df.shape[1] != 2:
        raise ValueError("CSV file must contain exactly two columns.")

    # Plot the bar graph
    try:
        ax = df.plot(kind='bar', x=df.columns[0], y=df.columns[1], legend=False)
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        plt.title('Bar Graph from CSV')
    except Exception as e:
        raise ValueError(f"Failed to plot bar graph: {e}")

    # Return the DataFrame and the Axes object
    return df, ax