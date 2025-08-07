from random import randint, seed
import matplotlib.pyplot as plt
import pandas as pd
import re

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars

def task_func(goals, penalties, rng_seed=None, teams=TEAMS):
    # Set the random seed for reproducibility
    if rng_seed is not None:
        seed(rng_seed)
    
    # Generate random goals and penalties for each team
    match_results = []
    for team in teams:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = team_penalties * PENALTY_COST
        match_results.append({
            'Team': team,
            'Goals': team_goals,
            'Penalty Cost': penalty_cost
        })
    
    # Create a DataFrame from the match results
    df = pd.DataFrame(match_results)
    
    # Analyze the data
    total_goals = df['Goals'].sum()
    total_penalty_cost = df['Penalty Cost'].sum()
    
    print(f"Total Goals: {total_goals}")
    print(f"Total Penalty Cost: ${total_penalty_cost:,}")
    
    # Visualize the data
    plt.figure(figsize=(12, 6))
    
    # Bar plot for goals
    plt.subplot(1, 2, 1)
    plt.bar(df['Team'], df['Goals'], color='skyblue')
    plt.xlabel('Team')
    plt.ylabel('Goals')
    plt.title('Goals Scored by Each Team')
    
    # Bar plot for penalty costs
    plt.subplot(1, 2, 2)
    plt.bar(df['Team'], df['Penalty Cost'], color='salmon')
    plt.xlabel('Team')
    plt.ylabel('Penalty Cost ($)')
    plt.title('Penalty Costs for Each Team')
    
    plt.tight_layout()
    plt.show()
    
    return df

# Example usage
df = task_func(goals=5, penalties=3, rng_seed=42)