import pandas as pd
from matplotlib import pyplot as plt

# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
GOALS_RANGE = (-10, 10)

def task_func(goals, penalties):
    # Calculate net scores
    net_scores = [g - p for g, p in zip(goals, penalties)]
    
    # Clip scores to stay within the specified range
    clipped_scores = [max(GOALS_RANGE[0], min(GOALS_RANGE[1], score)) for score in net_scores]
    
    # Create a DataFrame
    df = pd.DataFrame({'Team': TEAMS, 'Score': clipped_scores})
    
    # Visualize the results with a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Team'], df['Score'], color='skyblue')
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.title('Adjusted Scores for Each Team')
    plt.ylim(GOALS_RANGE)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    return df

# Example usage
goals = [12, 8, -5, 15, 3]
penalties = [2, 10, 3, 5, 0]
task_func(goals, penalties)
import unittest
# Unit Tests
class TestCases(unittest.TestCase):
    def test_no_goals_no_penalties(self):
        goals, penalties = {}, {}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [0] * 5})
        pd.testing.assert_frame_equal(task_func(goals, penalties), expected)
    def test_goals_no_penalties(self):
        goals = {team: index for index, team in enumerate(TEAMS, start=1)}
        penalties = {}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [1, 2, 3, 4, 5]})
        pd.testing.assert_frame_equal(task_func(goals, penalties), expected)
    def test_goals_with_penalties(self):
        goals = {team: 5 for team in TEAMS}
        penalties = {team: 2 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [3] * 5})
        pd.testing.assert_frame_equal(task_func(goals, penalties), expected)
    def test_clipping_negative_scores(self):
        goals = {team: -15 for team in TEAMS}
        penalties = {team: 0 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [-10] * 5})
        pd.testing.assert_frame_equal(task_func(goals, penalties), expected)
    def test_clipping_positive_scores(self):
        goals = {team: 20 for team in TEAMS}
        penalties = {team: 0 for team in TEAMS}
        expected = pd.DataFrame({'Team': TEAMS, 'Score': [10] * 5})
        pd.testing.assert_frame_equal(task_func(goals, penalties), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)