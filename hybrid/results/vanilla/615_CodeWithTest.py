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
import unittest
# Test Suite
class TestCases(unittest.TestCase):
    def setUp(self):
        self.teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        self.penalty_cost = 1000  # Match the PENALTY_COST used in task_func
    def test_goals_and_penalties_within_range(self):
        """Test that goals and penalties fall within specified ranges."""
        max_goals = 5
        max_penalties = 3
        df = task_func(max_goals, max_penalties)
        for _, row in df.iterrows():
            # Correctly extract goals and penalty cost from the 'Match Result' string
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            # Check if goals are within the expected range
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")
            # Calculate the maximum possible penalty cost and check it
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost,
                            f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")
    def test_negative_input_handling(self):
        """Test that negative inputs are handled correctly."""
        max_goals = -5
        max_penalties = -3
        df = task_func(max_goals, max_penalties)
        for _, row in df.iterrows():
            # Correctly extract and check values as before, ensuring no negative values are produced
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertTrue(0 <= goals, "Goals are negative which is not expected")
            self.assertTrue(0 <= penalty_cost, "Penalty cost is negative which is not expected")
    def test_zero_goals_and_penalties(self):
        """Test that the function handles 0 goals and 0 penalties correctly."""
        df = task_func(0, 0)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertEqual(goals, 0, "Goals should be 0 when max_goals is set to 0")
            self.assertEqual(penalty_cost, 0, "Penalty cost should be 0 when max_penalties is set to 0")
    def test_extremely_high_values(self):
        """Test the function with extremely high values for goals and penalties."""
        max_goals = 1000
        max_penalties = 500
        df = task_func(max_goals, max_penalties)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost, f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")
    def test_mixed_values(self):
        """Test the function with a mix of low and high values for goals and penalties."""
        max_goals = 10
        max_penalties = 1
        df = task_func(max_goals, max_penalties)
        for _, row in df.iterrows():
            match_result = row['Match Result']
            goals = int(match_result.split(' ')[0][1:])
            penalty_cost = int(match_result.split('$')[-1][:-1])
            self.assertTrue(0 <= goals <= max_goals, f"Goals {goals} not within range 0 to {max_goals}")
            max_penalty_cost = max_penalties * self.penalty_cost
            self.assertTrue(0 <= penalty_cost <= max_penalty_cost, f"Penalty cost {penalty_cost} not within range 0 to {max_penalty_cost}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)