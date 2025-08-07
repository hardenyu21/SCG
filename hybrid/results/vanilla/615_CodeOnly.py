from random import randint, seed
import pandas as pd

# Method
def task_func(goals, penalties, rng_seed=None):
    # Set the random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)
    
    # Define the cost of penalties
    penalty_cost = 100  # Example cost per penalty
    
    # Define the teams
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    
    # Initialize lists to store results
    team_results = []
    
    # Generate random results for each team
    for team in teams:
        # Randomly generate goals and penalties for the team
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        
        # Calculate the accumulated fines
        accumulated_fines = team_penalties * penalty_cost
        
        # Create the match result string
        match_result = f"Goals: {team_goals}, Fines: ${accumulated_fines}"
        
        # Append the result to the list
        team_results.append({'Team': team, 'Match Result': match_result})
    
    # Create a DataFrame from the results
    df = pd.DataFrame(team_results, columns=['Team', 'Match Result'])
    
    return df

# Example usage
df = task_func(goals=5, penalties=3, rng_seed=42)
print(df)