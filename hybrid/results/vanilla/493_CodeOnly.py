from datetime import datetime, timedelta
import random
import matplotlib.pyplot as plt

def task_func(
    epoch_milliseconds,
    teams=["Team1", "Team2", "Team3", "Team4", "Team5"],
    random_seed=0,
):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Convert epoch milliseconds to a datetime object
    start_date = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the number of days between the start date and the current date
    num_days = (current_date - start_date).days
    
    # Create a dictionary to store performance data for each team
    performance_data = {team: [] for team in teams}
    
    # Generate random performance data for each day
    for day in range(num_days + 1):
        current_day = start_date + timedelta(days=day)
        for team in teams:
            performance = random.uniform(0.1, 1.0)
            performance_data[team].append(performance)
    
    # Plot the performance trend for each team
    fig, ax = plt.subplots(figsize=(10, 6))
    for team in teams:
        ax.plot(range(num_days + 1), performance_data[team], label=team)
    
    ax.set_xlabel('Days since start date')
    ax.set_ylabel('Performance')
    ax.set_title('Performance Trend Over Time')
    ax.legend()
    ax.grid(True)
    
    # Show the plot
    plt.show()
    
    return performance_data, fig

# Example usage:
# epoch_milliseconds = 1609459200000  # Example epoch time for January 1, 2021
# performance_data, fig = task_func(epoch_milliseconds)