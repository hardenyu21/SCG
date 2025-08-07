import subprocess
import time
import json
import platform

LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Both 'interval' and 'duration' must be greater than zero.")
    
    start_time = time.time()
    end_time = start_time + duration
    cpu_usage_data = []

    while time.time() < end_time:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        cpu_usage = get_cpu_usage()
        cpu_usage_data.append({"timestamp": timestamp, "cpu_usage": cpu_usage})
        time.sleep(interval)

    try:
        with open(LOGFILE_PATH, 'w') as logfile:
            json.dump(cpu_usage_data, logfile, indent=4)
        return LOGFILE_PATH
    except IOError:
        return None

def get_cpu_usage():
    if platform.system() == "Windows":
        # Use 'wmic' command to get CPU usage on Windows
        result = subprocess.run(['wmic', 'cpu', 'get', 'loadpercentage'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract the percentage value from the output
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                return int(lines[1].strip())
    elif platform.system() == "Linux":
        # Use 'top' command to get CPU usage on Linux
        result = subprocess.run(['top', '-bn1', '-H'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract the percentage value from the output
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                cpu_usage_line = lines[1].split()
                return int(cpu_usage_line[8].strip('%'))
    
    return 0  # Default to 0% if unable to retrieve CPU usage
import unittest
import os
import json
from unittest.mock import patch
class TestCases(unittest.TestCase):
    """Test cases for task_func."""
    def setUp(self):
        """
        Setup before each test case.
        """
        self.logfile_path = "logfile.log"
    def tearDown(self):
        """
        Cleanup after each test case.
        """
        if os.path.exists(self.logfile_path):
            os.remove(self.logfile_path)
    @patch("time.time")
    def test_normal_operation(self, mock_time):
        """
        Test the normal operation of the function.
        It should create a log file with the expected content.
        """
        # Create an iterator that starts at 0 and increments by 5 every time it's called
        time_iter = iter(range(0, 100, 5))
        mock_time.side_effect = lambda: next(time_iter)
        result = task_func(5, 25)
        self.assertEqual(result, self.logfile_path)
        self.assertTrue(os.path.exists(self.logfile_path))
    def test_invalid_interval(self):
        """
        Test the function with an invalid interval value (less than or equal to zero).
        It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            task_func(-1, 10)
    def test_invalid_duration(self):
        """
        Test the function with an invalid duration value (less than or equal to zero).
        It should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            task_func(5, -10)
    @patch("subprocess.check_output")
    @patch("time.time")
    @patch("platform.system")
    def test_subprocess_output_handling_windows(
        self, mock_platform, mock_time, mock_subprocess
    ):
        """
        Test handling of subprocess output on Windows.
        It should correctly parse the CPU usage from the subprocess output.
        """
        mock_platform.return_value = "Windows"
        mock_time.side_effect = iter(range(0, 100, 5))
        mock_output = b'"\\Processor(_Total)\\% Processor Time","5.0"\n\n"2023-04-01 12:34:56.789","5.0"\n'
        mock_subprocess.return_value = mock_output
        result = task_func(5, 10)
        self.assertEqual(result, self.logfile_path)
    @patch("subprocess.check_output")
    @patch("time.time")
    @patch("platform.system")
    def test_subprocess_output_handling_linux(
        self, mock_platform, mock_time, mock_subprocess
    ):
        """
        Test handling of subprocess output on Linux.
        It should correctly parse the CPU usage from the subprocess output.
        """
        mock_platform.return_value = "Linux"
        mock_time.side_effect = iter(range(0, 100, 5))
        mock_output = b"Linux 4.15.0-54-generic (ubuntu) \nTasks: 195 total...\n%Cpu(s):  5.0 us,  2.0 sy,  0.0 ni, 92.0 id,  0.0 wa,  0.0 hi,  1.0 si,  0.0 st\n"
        mock_subprocess.return_value = mock_output
        result = task_func(5, 10)
        self.assertEqual(result, self.logfile_path)
    @patch("builtins.open", side_effect=IOError("Mocked error"))
    def test_io_error_handling(self, mock_open):
        """
        Test the function's behavior when an IOError occurs during file operations.
        It should handle the error and return None.
        """
        result = task_func(5, 10)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)