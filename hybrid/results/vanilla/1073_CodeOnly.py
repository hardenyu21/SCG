import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    seconds = []
    
    for time_str in time_strings:
        try:
            # Parse the time string according to the specified format
            parsed_time = time.strptime(time_str, time_format)
            # Extract the seconds component
            seconds.append(parsed_time.tm_sec)
        except ValueError:
            # If parsing fails, raise a ValueError
            raise ValueError(f"Time string '{time_str}' cannot be parsed according to format '{time_format}'.")
    
    # If all time strings are parsed successfully, plot the histogram
    fig, ax = plt.subplots()
    ax.hist(seconds, bins=range(61), edgecolor='black', align='left')
    ax.set_title('Histogram of Seconds Component')
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Frequency')
    plt.xticks(range(60))
    plt.grid(axis='y', alpha=0.75)
    
    # Show the plot
    plt.show()
    
    return ax

# Example usage:
# time_strings = ["01/01/2023 12:34:56.789000", "01/01/2023 12:34:57.123456"]
# ax = task_func(time_strings)