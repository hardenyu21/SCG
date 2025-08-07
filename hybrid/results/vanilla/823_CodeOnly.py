import time
import numpy as np

def task_func(samples=10, delay=0.1):
    delay_times = []

    for _ in range(samples):
        start_time = time.time()
        time.sleep(delay)
        end_time = time.time()
        
        actual_delay = end_time - start_time
        delay_times.append(actual_delay)

    mean_delay = np.mean(delay_times)
    std_dev_delay = np.std(delay_times)

    return (mean_delay, std_dev_delay)

# Example usage:
# mean, std_dev = task_func(samples=10, delay=0.1)
# print(f"Mean delay: {mean}, Standard deviation: {std_dev}")