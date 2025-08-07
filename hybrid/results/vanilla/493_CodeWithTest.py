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
import unittest
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.x = 1631295600000
        self.default_valid_teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]
    def _check_valid_performance_data(self, performance_data, valid_teams):
        self.assertIsInstance(performance_data, dict)
        self.assertTrue(all(team in valid_teams for team in performance_data.keys()))
        for team, performances in performance_data.items():
            for performance in performances:
                self.assertTrue(
                    0.1 <= performance <= 1, f"Performance out of range for {team}"
                )
                self.assertIsInstance(performance, float)
    def _check_plot(self, fig):
        ax = fig.axes[0]
        self.assertIsInstance(fig, plt.Figure)
        self.assertEqual(ax.get_ylabel(), "Performance")
        self.assertTrue(ax.get_xlabel().startswith("Days since"))
    def test_case_1(self):
        # Test basic case with default parameters - data
        performance_data, _ = task_func(self.x)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)
    def test_case_2(self):
        # Test basic case with default parameters - plot
        _, fig = task_func(self.x)
        self._check_plot(fig)
    def test_case_3(self):
        # Test basic case with custom input
        performance_data, fig = task_func(1236472051807, random_seed=42)
        self._check_plot(fig)
        self._check_valid_performance_data(performance_data, self.default_valid_teams)
    def test_case_4(self):
        # Test custom parameters - custom teams
        for custom_teams in [["A", "B"], ["c d e", "F", "GH", "ij kl"]]:
            performance_data, fig = task_func(self.x, teams=custom_teams, random_seed=42)
            self._check_plot(fig)
            self._check_valid_performance_data(performance_data, custom_teams)
    def test_case_5(self):
        # Test custom parameters - random seed
        performance_data1, _ = task_func(self.x, random_seed=42)
        performance_data2, _ = task_func(self.x, random_seed=42)
        performance_data3, _ = task_func(self.x, random_seed=0)
        self.assertEqual(performance_data1, performance_data2)
        self.assertNotEqual(performance_data1, performance_data3)
    def test_case_6(self):
        # Test error handling for invalid input time
        future_epoch = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)
        with self.assertRaises(ValueError):
            task_func(future_epoch)
    def test_case_7(self):
        # Test error handling for invalid team
        with self.assertRaises(TypeError):
            task_func(self.x, [1, 2, 3])
        with self.assertRaises(TypeError):
            task_func(self.x, [[]])
    def tearDown(self):
        plt.close("all")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)