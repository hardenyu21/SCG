from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

def task_func(activities):
    # Check if all activities are datetime objects
    if not all(isinstance(activity, datetime) for activity in activities):
        raise TypeError("All activities must be datetime objects.")
    
    # Dictionary to count activities per day of the week
    activity_count = defaultdict(int)
    
    # Count activities for each day of the week
    for activity in activities:
        day_of_week = activity.strftime('%A')  # Get the full name of the day
        activity_count[day_of_week] += 1
    
    # Days of the week in order
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Prepare data for plotting
    counts = [activity_count[day] for day in days_of_week]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(days_of_week, counts)
    
    # Set labels and title
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Number of Activities')
    ax.set_title('Weekly Activity')
    
    # Show the plot
    plt.show()
    
    return ax