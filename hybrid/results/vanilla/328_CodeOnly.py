import collections
import random

def task_func(number_teams=5):
    # Create a dictionary with team names and random points
    teams = {f"Team {i}": random.randint(0, 100) for i in range(1, number_teams + 1)}
    
    # Sort the dictionary by points in descending order
    sorted_teams = sorted(teams.items(), key=lambda item: item[1], reverse=True)
    
    # Convert the sorted list of tuples back to an OrderedDict
    ordered_teams = collections.OrderedDict(sorted_teams)
    
    return ordered_teams

# Example usage
print(task_func(5))