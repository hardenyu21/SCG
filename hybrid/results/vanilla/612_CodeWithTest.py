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
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    @patch(__name__ + '.choice', return_value=400)
    def test_goals_greater_than_penalties(self, mock_choice):
        goals = {'Team A': 4, 'Team B': 2, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 1, 'Team B': 1, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        expected_data = {
            'Team': TEAMS,
            'Goals': [4, 2, 0, 0, 0],
            'Penalties': [1, 1, 0, 0, 0],
            'Penalties Cost': [400, 400, 0, 0, 0],  # Mocked value is reflected here
            'Performance Score': [3, 1, 0, 0, 0]  # Assuming Performance Score is Goals - Penalties
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))
    @patch(__name__ + '.choice', return_value=200)
    def test_some_teams_missing(self, mock_choice):
        goals = {'Team A': 2, 'Team E': 5}
        penalties = {'Team A': 0, 'Team E': 3}
        expected_data = {
            'Team': TEAMS,
            'Goals': [2, 0, 0, 0, 5],
            'Penalties': [0, 0, 0, 0, 3],
            'Penalties Cost': [0, 0, 0, 0, 600],
            'Performance Score': [2, 0, 0, 0, 2]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)
    @patch(__name__ + '.choice', return_value=500)
    def test_penalties_greater_than_goals(self, mock_choice):
        goals = {'Team B': 1, 'Team D': 2}
        penalties = {'Team B': 3, 'Team D': 5}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 1, 0, 2, 0],
            'Penalties': [0, 3, 0, 5, 0],
            'Penalties Cost': [0, 1500, 0, 2500, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)
    @patch(__name__ + '.choice', return_value=300)
    def test_all_teams_penalty(self, mock_choice):
        goals = {'Team A': 0, 'Team B': 0, 'Team C': 0, 'Team D': 0, 'Team E': 0}
        penalties = {'Team A': 2, 'Team B': 1, 'Team C': 3, 'Team D': 1, 'Team E': 4}
        expected_penalties_cost = [penalty * mock_choice.return_value for penalty in penalties.values()]
        expected_data = {
            'Team': list(goals.keys()),  # The list of teams from the goals dictionary keys
            'Goals': list(goals.values()),  # The list of goals from the goals dictionary values
            'Penalties': list(penalties.values()),  # The list of penalties from the penalties dictionary values
            'Penalties Cost': expected_penalties_cost,
            'Performance Score': [0] * len(TEAMS)  # A list of zeros for performance score
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))
    @patch(__name__ + '.choice', return_value=100)
    def test_empty_goals_and_penalties(self, mock_choice):
        goals = {}
        penalties = {}
        expected_data = {
            'Team': TEAMS,
            'Goals': [0, 0, 0, 0, 0],
            'Penalties': [0, 0, 0, 0, 0],
            'Penalties Cost': [0, 0, 0, 0, 0],
            'Performance Score': [0, 0, 0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)
    @patch(__name__ + '.choice', return_value=300)
    def test_no_penalties(self, mock_choice):
        goals = {'Team A': 3, 'Team B': 2}
        penalties = {'Team A': 0, 'Team B': 0}
        expected_data = {
            'Team': ['Team A', 'Team B'] + ['Team C', 'Team D', 'Team E'],
            'Goals': [3, 2] + [0, 0, 0],
            'Penalties': [0, 0] + [0, 0, 0],
            'Penalties Cost': [0, 0] + [0, 0, 0],
            'Performance Score': [3, 2] + [0, 0, 0]
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(goals, penalties)
        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)