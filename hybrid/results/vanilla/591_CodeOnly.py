from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'

def task_func(hours, file_path=FILE_PATH):
    # Initialize data dictionary
    data = {
        'Time': [],
        'Temperature': [],
        'Category': []
    }
    
    # Generate temperature data for the specified number of hours
    current_time = datetime.now()
    for _ in range(hours):
        # Generate a random temperature between -10 and 40 degrees Celsius
        temperature = randint(-10, 40)
        
        # Determine the temperature category
        if temperature < 10:
            category = TEMP_CATEGORIES[0]  # Cold
        elif temperature < 30:
            category = TEMP_CATEGORIES[1]  # Normal
        else:
            category = TEMP_CATEGORIES[2]  # Hot
        
        # Append data to the dictionary
        data['Time'].append(current_time.strftime('%Y-%m-%d %H:%M:%S'))
        data['Temperature'].append(temperature)
        data['Category'].append(category)
        
        # Increment the time by one hour
        current_time += timedelta(hours=1)
    
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    
    # Plot the temperature data
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Temperature'], marker='o', linestyle='-')
    ax.set_title('Temperature Data Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return the file path and the plot object
    return file_path, ax

# Example usage:
# file_path, ax = task_func(24)
# plt.show()