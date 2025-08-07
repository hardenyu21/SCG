from random import choice
import numpy as np
import pandas as pd

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]

def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    # Ensure goals and penalties are lists of the same length as teams
    if len(goals) != len(teams) or len(penalties) != len(teams):
        raise ValueError("The length of goals, penalties, and teams must be the same.")
    
    # Initialize lists to store the results
    penalties_cost = []
    performance_score = []
    
    # Calculate penalties cost and performance score for each team
    for i in range(len(teams)):
        # Randomly select a penalty cost multiplier
        penalty_cost_multiplier = choice(penalties_costs)
        
        # Calculate penalties cost
        penalties_cost.append(penalties[i] * penalty_cost_multiplier)
        
        # Calculate performance score
        performance_score.append(max(goals[i] - penalties[i], 0))
    
    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Team': teams,
        'Goals': goals,
        'Penalties': penalties,
        'Penalties Cost': penalties_cost,
        'Performance Score': performance_score
    })
    
    return df

# Example usage
goals = [10, 15, 8, 12, 9]
penalties = [3, 5, 7, 2, 6]
performance_report = task_func(goals, penalties)
print(performance_report)