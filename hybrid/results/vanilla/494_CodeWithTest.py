from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Initialize Faker with a seed for reproducibility
    fake = Faker()
    Faker.seed(seed)
    
    # Convert epoch milliseconds to datetime object in the current system timezone
    current_timezone = datetime.now().astimezone().tzinfo
    event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000, current_timezone)
    
    # Generate a fake event name
    event_name = fake.catch_phrase()
    
    # Validate and filter timezones
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones:
            valid_timezones.append(tz)
        elif re.match(r'^UTC[+-]\d{2}:\d{2}$', tz):
            valid_timezones.append(tz)
    
    # If no valid timezones are provided, use UTC
    if not valid_timezones:
        valid_timezones = ["UTC"]
    
    # Randomly select a valid timezone
    selected_timezone = fake.random_element(valid_timezones)
    
    # Create the event schedule
    event_schedule = {
        'date': event_datetime.strftime('%Y-%m-%d'),
        'time': event_datetime.strftime('%H:%M:%S'),
        'timezone': selected_timezone
    }
    
    # Return the dictionary with the fake event name and schedule
    return {event_name: [event_schedule]}

# Example usage:
# epoch_milliseconds = 1633072800000  # Example epoch time in milliseconds
# print(task_func(epoch_milliseconds))
import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    TIMEZONES = ["UTC", "UTC+01:00", "UTC+02:00", "UTC+03:00", "UTC+04:00", "UTC+05:00"]
    default_time = 1236472051807
    def check_structure_and_content(self, schedule, epoch_milliseconds):
        event_name = list(schedule.keys())[0]
        event_details = schedule[event_name]
        event_datetime = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
        self.assertIsInstance(schedule, dict)
        self.assertEqual(len(schedule), 1)
        self.assertEqual(len(event_details), 1)
        self.assertEqual(event_details[0]["date"], event_datetime.date())
        self.assertEqual(event_details[0]["time"], event_datetime.time())
        self.assertIn(
            event_details[0]["timezone"], self.TIMEZONES
        )  # expected in these tests
    def test_case_1(self):
        # Test defaults
        epoch_milliseconds = self.default_time
        schedule = task_func(epoch_milliseconds)
        self.check_structure_and_content(schedule, epoch_milliseconds)
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
    def test_case_2(self):
        # Test with a specific known epoch
        epoch_milliseconds = self.default_time
        schedule = task_func(epoch_milliseconds, seed=2, timezones=self.TIMEZONES)
        self.check_structure_and_content(schedule, epoch_milliseconds)
    def test_case_3(self):
        # Test with an invalid timezone list - should default to UTC
        schedule = task_func(self.default_time, seed=3, timezones=["INVALID"])
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
        schedule = task_func(self.default_time, seed=3, timezones=["FOO", "BAR"])
        self.assertTrue(schedule[list(schedule.keys())[0]][0]["timezone"] == "UTC")
        for valid_tz in self.TIMEZONES:
            schedule = task_func(self.default_time, seed=3, timezones=["INVALID", valid_tz])
            self.assertTrue(
                schedule[list(schedule.keys())[0]][0]["timezone"] == valid_tz,
                f'Expected {valid_tz}, got {schedule[list(schedule.keys())[0]][0]["timezone"]}',
            )
    def test_case_4(self):
        # Test random seed reproducibility
        schedule1 = task_func(self.default_time, seed=42, timezones=self.TIMEZONES)
        schedule2 = task_func(self.default_time, seed=42, timezones=self.TIMEZONES)
        self.assertEqual(schedule1, schedule2)
    def test_case_6(self):
        # Test handling invalid dates - invalid types
        for invalid in ["1", [], None]:
            with self.assertRaises(TypeError):
                task_func(invalid)
    def test_case_7(self):
        # Test handling extremely future dates
        epoch_milliseconds = (
            4133980800000  # This is a date far in the future (2100-12-31)
        )
        schedule = task_func(epoch_milliseconds, seed=5, timezones=["UTC", "UTC+05:00"])
        self.check_structure_and_content(schedule, epoch_milliseconds)
        # No additional asserts required, check_structure_and_content will validate
    def test_case_8(self):
        # Test handling leap year date
        epoch_milliseconds = 1582934400000  # This corresponds to 2020-02-29
        schedule = task_func(
            epoch_milliseconds, seed=6, timezones=["UTC", "UTC+01:00", "UTC+02:00"]
        )
        self.check_structure_and_content(schedule, epoch_milliseconds)
        # Validate it handles the leap day correctly
        event_date = schedule[list(schedule.keys())[0]][0]["date"]
        self.assertTrue(event_date.year == 2020)
        self.assertTrue(event_date.month == 2)
        self.assertTrue(event_date.day == 29)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)