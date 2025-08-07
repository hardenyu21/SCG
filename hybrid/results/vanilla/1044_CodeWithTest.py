
import unittest
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_future_date_valid_booking_data(self):
        """
        Test task_func with a future date and valid booking data.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {"Room1": "Booked", "Room2": "Available"}
        report_df, _ = task_func(future_date, booking_data)
        self.assertIn("Room1", report_df["Room"].values)
        self.assertIn("Booked", report_df["Booking Status"].values)
    def test_past_date(self):
        """
        Test task_func with a past date to ensure it raises a ValueError.
        """
        past_date = "2020-01-01"
        booking_data = {"Room1": "Booked"}
        with self.assertRaises(ValueError):
            task_func(past_date, booking_data)
    def test_invalid_date_format(self):
        """
        Test task_func with an invalid date format to check for ValueError.
        """
        invalid_date = "15-06-2023"
        booking_data = {"Room1": "Booked"}
        with self.assertRaises(ValueError):
            task_func(invalid_date, booking_data)
    def test_booking_data_for_nonexistent_room(self):
        """
        Test task_func with booking data for a room not in the ROOMS constant.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {"Room6": "Booked"}
        report_df, _ = task_func(future_date, booking_data)
        self.assertIn("Not Listed", report_df["Booking Status"].values)
    def test_no_booking_data(self):
        """
        Test task_func with no booking data provided.
        """
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        booking_data = {}
        report_df, _ = task_func(future_date, booking_data)
        self.assertTrue((report_df["Booking Status"] == "Not Listed").all())
    def tearDown(self):
        plt.clf()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)