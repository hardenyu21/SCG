import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

def task_func(duration):
    timestamps = []
    random_values = []
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        random_value = randint(0, 100)
        
        timestamps.append(current_time)
        random_values.append(random_value)
        
        # Print the current timestamp and random value for real-time monitoring
        print(f"Time: {current_time}, Value: {random_value}")
        
        # Sleep for a short duration to simulate real-time data generation
        time.sleep(0.1)
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, random_values, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Random Value')
    plt.title('Real-time Random Data Generation')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return (timestamps, random_values)

# Example usage:
# task_func(10)  # Generate random data for 10 seconds