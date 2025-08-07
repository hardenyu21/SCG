from datetime import datetime
import random
import matplotlib.pyplot as plt

def task_func(date_str):
    # Parse the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Get the day of the month
    day_of_month = date.day
    
    # Generate a list of random integers with the count equal to the day of the month
    random_integers = [random.randint(0, 100) for _ in range(day_of_month)]
    
    # Create a line plot of the random integers
    fig, ax = plt.subplots()
    ax.plot(random_integers, marker='o')
    
    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Random Integer')
    ax.set_title(f'Random Integers for {date_str}')
    
    # Return the Axes object
    return ax