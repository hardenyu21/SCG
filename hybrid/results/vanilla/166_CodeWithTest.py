import pandas as pd
from datetime import datetime, timedelta
import holidays

def task_func(start_date=datetime(2023, 1, 1), end_date=datetime(2023, 12, 31), country='US'):
    # Validate input dates
    if not isinstance(start_date, datetime):
        raise ValueError("start_date must be a datetime object.")
    if not isinstance(end_date, datetime):
        raise ValueError("end_date must be a datetime object.")
    if start_date > end_date:
        raise ValueError("start_date must not be after end_date.")
    if end_date < start_date:
        raise ValueError("end_date must not be before start_date.")
    
    # Create a range of dates from start_date to end_date
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Get public holidays for the specified country
    try:
        country_holidays = holidays.CountryHoliday(country, years=[start_date.year, end_date.year])
    except KeyError:
        raise ValueError(f"Invalid country code: {country}")
    
    # Filter out weekends and public holidays
    business_days = [
        date for date in date_range
        if date.weekday() < 5 and date not in country_holidays
    ]
    
    return business_days

# Example usage:
# business_days = task_func(datetime(2023, 1, 1), datetime(2023, 12, 31), 'US')
# print(business_days)
import unittest
from datetime import datetime
class TestCases(unittest.TestCase):
    def test_default_dates(self):
        result = task_func()
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(d, datetime) for d in result))
        self.assertNotIn(datetime(2023, 1, 1), result)  # New Year's Day, a holiday
    
    def test_custom_dates(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 3)
        result = task_func(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 3)], result)  # A business day
    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            task_func(end_date=datetime(2022, 12, 31))  # end_date before default start_date
    def test_invalid_date_types(self):
        with self.assertRaises(ValueError):
            task_func(start_date="2023-01-01", end_date="2023-12-31")  # String dates
    def test_non_default_country(self):
        # Testing with a different country's holidays (e.g., UK)
        result = task_func(country='GB')
        self.assertNotIn(datetime(2023, 4, 7), result)  # Good Friday in UK
    def test_range_including_weekend(self):
        start_date = datetime(2023, 1, 6)  # Friday
        end_date = datetime(2023, 1, 9)    # Monday
        result = task_func(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 6), datetime(2023, 1, 9)], result)
    def test_range_including_public_holiday(self):
        start_date = datetime(2023, 7, 3)  # Day before Independence Day
        end_date = datetime(2023, 7, 5)    # Day after Independence Day
        result = task_func(start_date, end_date)
        # print(result)
        self.assertEqual([datetime(2023, 7, 3), datetime(2023, 7, 5)], result)  # July 4th is excluded
    def test_short_business_week(self):
        start_date = datetime(2023, 11, 20)  # Week of Thanksgiving
        end_date = datetime(2023, 11, 24)
        result = task_func(start_date, end_date)
        # print(result)
        self.assertEqual([datetime(2023, 11, 20), datetime(2023, 11, 21), datetime(2023, 11, 22),datetime(2023, 11, 24)], result)
    def test_single_day_range_business_day(self):
        start_date = end_date = datetime(2023, 1, 3)  # A Tuesday
        result = task_func(start_date, end_date)
        self.assertEqual([datetime(2023, 1, 3)], result)
    def test_single_day_range_non_business_day(self):
        start_date = end_date = datetime(2023, 1, 1)  # A Sunday
        result = task_func(start_date, end_date)
        self.assertEqual([], result)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)