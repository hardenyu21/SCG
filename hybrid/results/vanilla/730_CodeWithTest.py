import pickle
import os
from datetime import datetime

# Constants
FILE_NAME = 'save.pkl'

def task_func(dt):
    # Save the datetime object to a pickle file
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    # Load the datetime object back from the pickle file
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)
    
    # Return the loaded datetime object
    return loaded_dt

# Example usage:
# dt = datetime.now()
# loaded_dt = task_func(dt)
# print("Original datetime:", dt)
# print("Loaded datetime:", loaded_dt)
import unittest
from datetime import datetime
import pytz
class TestCases(unittest.TestCase):
    def test_datetime_saving_and_loading(self):
        # Test saving and loading the current datetime with UTC timezone
        dt = datetime.now(pytz.UTC)
        loaded_dt = task_func(dt)
        self.assertEqual(dt, loaded_dt, "The loaded datetime object should match the original")
    def test_timezone_awareness(self):
        # Test saving and loading a timezone-aware datetime object
        tz = pytz.timezone('Asia/Tokyo')
        dt = datetime.now(tz)
        loaded_dt = task_func(dt)
        self.assertEqual(dt, loaded_dt, "The loaded datetime object should be timezone aware and match the original")
    def test_file_cleanup(self):
        # Test whether the pickle file is properly cleaned up
        dt = datetime.now(pytz.UTC)
        task_func(dt)
        self.assertFalse(os.path.exists(FILE_NAME), "The pickle file should be cleaned up after loading")
    def test_naive_datetime(self):
        # Test saving and loading a naive datetime object
        dt = datetime.now()
        loaded_dt = task_func(dt)
        self.assertEqual(dt, loaded_dt, "The loaded datetime object should match the original naive datetime")
        self.assertIsNone(loaded_dt.tzinfo, "The loaded datetime object should be naive (no timezone)")
    def test_different_timezones(self):
        # Test saving and loading datetime objects with different timezones
        tz1 = pytz.timezone('US/Eastern')
        tz2 = pytz.timezone('Europe/London')
        dt1 = datetime.now(tz1)
        dt2 = datetime.now(tz2)
        loaded_dt1 = task_func(dt1)
        loaded_dt2 = task_func(dt2)
        self.assertEqual(dt1, loaded_dt1, "The loaded datetime object should match the original (US/Eastern)")
        self.assertEqual(dt2, loaded_dt2, "The loaded datetime object should match the original (Europe/London)")
        self.assertEqual(dt1.tzinfo, loaded_dt1.tzinfo, "The loaded datetime object should have the same timezone (US/Eastern)")
        self.assertEqual(dt2.tzinfo, loaded_dt2.tzinfo, "The loaded datetime object should have the same timezone (Europe/London)")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)