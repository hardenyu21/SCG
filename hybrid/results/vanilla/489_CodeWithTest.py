import pandas as pd
from datetime import datetime, timedelta
import random

def task_func(epoch_milliseconds, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Convert epoch milliseconds to a datetime object
    start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Get the current system time
    current_time = datetime.now()
    
    # Check if the start time is after the current system time
    if start_time > current_time:
        raise ValueError("The start time is after the current system time.")
    
    # Predefined lists for users and activities
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    activities = ['login', 'logout', 'browse', 'search', 'purchase']
    
    # Initialize a list to store log entries
    logs = []
    
    # Initialize the current time for logging
    current_log_time = start_time
    
    # Generate log entries until the current system time
    while current_log_time <= current_time:
        # Randomly choose a user and an activity
        user = random.choice(users)
        activity = random.choice(activities)
        
        # Append the log entry to the list
        logs.append({
            'User': user,
            'Activity': activity,
            'Time': current_log_time
        })
        
        # Increment the current log time by a random number of seconds (1 to 10)
        increment_seconds = random.randint(1, 10)
        current_log_time += timedelta(seconds=increment_seconds)
    
    # Create a DataFrame from the log entries
    df = pd.DataFrame(logs)
    
    return df
import unittest
import pandas as pd
from datetime import datetime, timedelta
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic functionality - 1 day ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        self.assertTrue(isinstance(log, pd.DataFrame))
        self.assertTrue("User" in log.columns)
        self.assertTrue("Activity" in log.columns)
        self.assertTrue("Time" in log.columns)
        start_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertEqual(log.iloc[0]["Time"], start_time)
    def test_case_2(self):
        # Test with a short time frame - 1 minutes ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(minutes=1)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        self.assertTrue(len(log) > 0)  # Should have at least one entry
        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )
    def test_case_3(self):
        # Test with a specific seed
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=1)).timestamp() * 1000
        )
        seed = 42
        log = task_func(epoch_milliseconds, seed=seed)
        first_row = log.iloc[0]
        expected_user = "user1"
        expected_activity = "login"
        self.assertEqual(first_row["User"], expected_user)
        self.assertEqual(first_row["Activity"], expected_activity)
    def test_case_4(self):
        # Test functionality over a longer period - 1 month ago
        epoch_milliseconds = int(
            (datetime.now() - timedelta(days=30)).timestamp() * 1000
        )
        log = task_func(epoch_milliseconds)
        # Ensure that log timestamps are properly incrementing
        time_diffs = log["Time"].diff().dropna()
        self.assertTrue(all(time_diffs > timedelta(seconds=0)))
        seconds_in_a_month = (
            30 * 24 * 60 * 60
        )  # Approximate number of seconds in a month
        max_possible_entries = (
            seconds_in_a_month  # Assuming a minimum of 1-second increments
        )
        min_possible_entries = (
            seconds_in_a_month // 10
        )  # Assuming a maximum of 10-second increments
        # Verify that the log has a reasonable number of entries given the time frame
        self.assertTrue(min_possible_entries <= len(log) <= max_possible_entries)
        self.assertTrue(
            log["Time"].min() >= datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        )
        self.assertTrue(log["Time"].max() <= datetime.now())
    def test_case_5(self):
        # Test invalid start time (future)
        epoch_milliseconds = int(
            (datetime.now() + timedelta(days=1)).timestamp() * 1000
        )
        with self.assertRaises(Exception):
            task_func(epoch_milliseconds)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)