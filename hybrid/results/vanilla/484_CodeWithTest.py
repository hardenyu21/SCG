import math
import numpy as np
from datetime import datetime, timedelta
import pandas as pd

def task_func(
    start_time,
    end_time,
    step,
    columns=["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
    sensor_statuses=["OK", "MAINTENANCE_REQUIRED", "ERROR"],
    random_seed=42,
):
    # Set the random seed for reproducibility
    np.random.seed(random_seed)
    
    # Convert start_time and end_time to datetime objects if they are not already
    if isinstance(start_time, str):
        start_time = datetime.fromisoformat(start_time)
    if isinstance(end_time, str):
        end_time = datetime.fromisoformat(end_time)
    
    # Generate timestamps
    timestamps = []
    current_time = start_time
    while current_time <= end_time:
        timestamps.append(current_time)
        current_time += timedelta(seconds=step)
    
    # Prepare data for the DataFrame
    data = {col: [] for col in columns}
    
    for timestamp in timestamps:
        # Convert timestamp to seconds since epoch
        seconds = (timestamp - datetime(1970, 1, 1)).total_seconds()
        
        # Generate sensor readings with noise
        sensor1_value = math.sin(seconds) + np.random.normal(0, 0.1)
        sensor2_value = math.cos(seconds) + np.random.normal(0, 0.1)
        sensor3_value = math.tan(seconds) + np.random.normal(0, 0.1)
        
        # Randomly choose a sensor status
        sensor_status = np.random.choice(sensor_statuses)
        
        # Append data to the respective lists
        data[columns[0]].append(timestamp)
        data[columns[1]].append(sensor1_value)
        data[columns[2]].append(sensor2_value)
        data[columns[3]].append(sensor3_value)
        data[columns[4]].append(sensor_status)
    
    # Create and return the DataFrame
    return pd.DataFrame(data)

# Example usage:
# df = task_func("2023-01-01T00:00:00", "2023-01-01T00:01:00", 10)
# print(df)
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        df = task_func(0, 10000, 100, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(
            list(df.columns),
            ["Timestamp", "Sensor1", "Sensor2", "Sensor3", "SensorStatus"],
        )
        self.assertTrue(
            (df["SensorStatus"].isin(["OK", "MAINTENANCE_REQUIRED", "ERROR"])).all()
        )
    def test_case_2(self):
        # Test custom columns
        columns = ["Time", "Sensor_A", "Sensor_B", "Sensor_C", "Status"]
        statuses = ["WORKING", "NEEDS_CHECK", "FAILED"]
        df = task_func(
            1500, 3000, 50, columns=columns, sensor_statuses=statuses, random_seed=42
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(list(df.columns), columns)
        self.assertTrue((df["Status"].isin(statuses)).all())
    def test_case_3(self):
        # Test generated data integrity by comparing with expected results
        np.random.seed(42)
        ts = 0  # Using the starting timestamp for simplicity
        expected_sensor1 = math.sin(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor2 = math.cos(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        expected_sensor3 = math.tan(ts / 1000) + np.random.normal(0, 0.1, 1)[0]
        df = task_func(0, 100, 100, random_seed=42)
        self.assertAlmostEqual(df.iloc[0]["Sensor1"], expected_sensor1, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor2"], expected_sensor2, places=5)
        self.assertAlmostEqual(df.iloc[0]["Sensor3"], expected_sensor3, places=5)
    def test_case_4(self):
        # Test handling invalid start times
        with self.assertRaises(ValueError):
            task_func(10000, 0, 100)
    def test_case_5(self):
        # Test handling incorrect end times
        with self.assertRaises(ValueError):
            task_func(1000, 900, 100)
    def test_case_6(self):
        # Test column handling
        columns = ["Time", "Value1", "Value2", "Value3", "MachineStatus"]
        df = task_func(0, 500, 100, columns=columns)
        self.assertEqual(list(df.columns), columns)
        # Too few/too many columns
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, columns[:-1])
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, columns + ["foo", "bar"])
    def test_case_7(self):
        # Test sensor status handling
        with self.assertRaises(ValueError):
            task_func(0, 500, 100, [])
        statuses = ["RUNNING", "SHUTDOWN", "ERROR"]
        df = task_func(0, 500, 100, sensor_statuses=statuses)
        self.assertTrue((df["SensorStatus"].isin(statuses)).all())
    def test_case_8(self):
        # Test random seed
        df1 = task_func(0, 500, 100, random_seed=42)
        df2 = task_func(0, 500, 100, random_seed=42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_case_9(self):
        # Test invalid steps handling
        with self.assertRaises(ValueError):
            task_func(0, 1000, -100)  # Step is negative
        with self.assertRaises(ValueError):
            task_func(0, 1000, 0)  # Step is zero


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)