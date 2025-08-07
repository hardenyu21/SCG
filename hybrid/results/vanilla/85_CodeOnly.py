import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def task_func(start_date, end_date, random_seed=42):
    # Validate date range
    if end_date < start_date:
        raise ValueError("end_date must be after start_date")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Generate random weather data
    temperature = np.random.uniform(-10, 40, size=len(date_range))
    humidity = np.random.uniform(20, 100, size=len(date_range))
    wind_speed = np.random.uniform(0, 20, size=len(date_range))
    
    # Create DataFrame
    weather_data = pd.DataFrame({
        'Date': date_range,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed
    })
    
    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature (°C)', color='r')
    ax.plot(weather_data['Date'], weather_data['Humidity'], label='Humidity (%)', color='g')
    ax.plot(weather_data['Date'], weather_data['Wind Speed'], label='Wind Speed (m/s)', color='b')
    
    ax.set_title('Simulated Weather Data')
    ax.set_xlabel('Date')
    ax.set_ylabel('Values')
    ax.legend()
    ax.grid(True)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Return DataFrame and plot object
    return weather_data, ax

# Example usage:
# df, ax = task_func('2023-01-01', '2023-01-10')
# plt.show()