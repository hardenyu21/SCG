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
import unittest
# Unit Tests
class TestCases(unittest.TestCase):
    def setUp(self):
        self.expected_columns = ['Team', 'Match Result', 'Goals', 'Penalty Cost']
    def test_dataframe_structure(self):
        """Test if the DataFrame contains the expected structure."""
        df = task_func(4, 2, rng_seed=1)
        self.assertListEqual(list(df.columns), self.expected_columns)
    def test_randomness_control(self):
        """Test if the rng_seed parameter controls randomness."""
        df1 = task_func(4, 2, rng_seed=42)
        df2 = task_func(4, 2, rng_seed=42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_positive_goals_penalties(self):
        """Test for positive goals and penalties input."""
        df = task_func(5, 3, rng_seed=2)
        self.assertTrue((df['Goals'] >= 0).all() and (df['Goals'] <= 5).all())
        self.assertTrue((df['Penalty Cost'] % PENALTY_COST == 0).all())
    def test_zero_goals_penalties(self):
        """Test for zero goals and penalties."""
        df = task_func(0, 0, rng_seed=3)
        self.assertTrue((df['Goals'] == 0).all())
        self.assertTrue((df['Penalty Cost'] == 0).all())
    def test_no_teams(self):
        """Test function with no teams."""
        df = task_func(5, 3, rng_seed=4, teams=[])
        self.assertTrue(df.empty)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)