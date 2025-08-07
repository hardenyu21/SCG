import re
from datetime import datetime, time

def task_func(logs: list):
    error_times = []
    
    # Regular expression to find error logs and extract time
    error_pattern = re.compile(r'ERROR.*?(\d{2}:\d{2}:\d{2})')
    
    for log in logs:
        match = error_pattern.search(log)
        if match:
            # Extract the time string and convert it to a datetime.time object
            time_str = match.group(1)
            error_time = datetime.strptime(time_str, '%H:%M:%S').time()
            error_times.append(error_time)
    
    # Calculate the average time of occurrence of errors
    if error_times:
        total_seconds = sum((dt.hour * 3600 + dt.minute * 60 + dt.second) for dt in error_times)
        average_seconds = total_seconds // len(error_times)
        average_time = time(hour=average_seconds // 3600, minute=(average_seconds % 3600) // 60, second=average_seconds % 60)
    else:
        average_time = None
    
    return error_times, average_time

# Example usage:
logs = [
    "2023-10-01 12:34:56 INFO: System started",
    "2023-10-01 12:35:01 ERROR: Failed to load module",
    "2023-10-01 12:36:00 INFO: Processing data",
    "2023-10-01 12:37:00 ERROR: Connection timeout",
    "2023-10-01 12:38:00 INFO: Data processed"
]

error_times, average_time = task_func(logs)
print("Error Times:", error_times)
print("Average Time of Errors:", average_time)
import unittest
from datetime import time
class TestCases(unittest.TestCase):
    def test_case_1(self):
        logs = ['2021-06-15 09:45:00 ERROR: Failed to connect to database',
                '2021-06-15 10:15:00 WARNING: Low disk space',
                '2021-06-15 10:35:00 INFO: Backup completed successfully']
        result = task_func(logs)
        self.assertEqual(result, ([time(9, 45)], time(9, 45)))
    def test_case_2(self):
        logs = ['2021-06-15 08:45:00 ERROR: Failed to authenticate',
                '2021-06-15 09:15:00 ERROR: Failed to connect to database',
                '2021-06-15 10:35:00 INFO: Backup completed successfully']
        result = task_func(logs)
        self.assertEqual(result, ([time(8, 45), time(9, 15)], time(9, 0)))
    def test_case_3(self):
        logs = ['2021-06-15 07:45:00 INFO: Backup started',
                '2021-06-15 08:15:00 WARNING: Low memory',
                '2021-06-15 09:35:00 INFO: Backup completed successfully']
        result = task_func(logs)
        self.assertEqual(result, ([], time(0, 0)))
    def test_case_4(self):
        logs = []
        result = task_func(logs)
        self.assertEqual(result, ([], time(0, 0)))
    def test_case_5(self):
        logs = ['2021-06-15 09:45:00 ERROR: Failed to connect to database',
                '2021-06-15 10:15:00 WARNING: Low disk space',
                '2021-06-15 11:45:00 ERROR: Failed to authenticate']
        result = task_func(logs)
        self.assertEqual(result, ([time(9, 45), time(11, 45)], time(10, 45)))
    def test_case_invalid_format(self):
        logs = ['Invalid log format',
                'Another invalid log format',
                'Yet another invalid log format']
        result = task_func(logs)
        self.assertEqual(result, ([], time(0, 0)))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)