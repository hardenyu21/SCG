import pandas as pd
import numpy as np

def task_func(fruit_data):
    if not fruit_data:
        return pd.DataFrame(columns=['Total Count', 'Average Count'])

    # Create a dictionary to store total and count for each fruit
    fruit_totals = {}

    for fruit, count in fruit_data:
        if fruit in fruit_totals:
            fruit_totals[fruit]['total'] += count
            fruit_totals[fruit]['count'] += 1
        else:
            fruit_totals[fruit] = {'total': count, 'count': 1}

    # Calculate total and average counts
    data = {
        'Total Count': [],
        'Average Count': []
    }
    for fruit, values in fruit_totals.items():
        total_count = values['total']
        average_count = total_count / values['count']
        data['Total Count'].append(total_count)
        data['Average Count'].append(average_count)

    # Create a DataFrame
    df = pd.DataFrame(data, index=fruit_totals.keys())
    return df
import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    test_data_sets = [
        [('vote', 19), ('those', 15), ('recent', 4), ('manage', 12), ('again', 13), ('box', 16), ('box', 16), ('box', 16)],
        [('experience', 14), ('interesting', 8), ('firm', 13), ('enjoy', 19), ('area', 3), ('what', 12), ('along', 1)],
        [('our', 11), ('then', 2), ('imagine', 6), ('heavy', 17), ('low', 6), ('site', 12), ('nearly', 3), ('organization', 6), ('me', 14), ('eat', 17)],
        [('involve', 2), ('money', 11), ('use', 15), ('fish', 19), ('boy', 3), ('both', 10)], [('take', 16), ('activity', 12), ('tend', 10), ('take', 2)]
    ]
    def test_empty(self):
        report = task_func([])
        self.assertTrue(report.empty)
    def test_case_1(self):
        # Using the first set of test data
        report = task_func(self.test_data_sets[0])
        expected = pd.DataFrame(
            {
            'Total Count': {'vote': 19,
            'those': 15,
            'recent': 4,
            'manage': 12,
            'again': 13,
            'box': 48},
            'Average Count': {'vote': 19.0,
            'those': 15.0,
            'recent': 4.0,
            'manage': 12.0,
            'again': 13.0,
            'box': 16.0}
            }
        )
        # The report should be a DataFrame with the correct columns and index
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_2(self):
        # Using the second set of test data
        report = task_func(self.test_data_sets[1])
        expected = pd.DataFrame(
            {'Total Count': {'experience': 14.0,
                'interesting': 8.0,
                'firm': 13.0,
                'enjoy': 19.0,
                'area': 3.0,
                'what': 12.0,
                'along': 1.0},
                'Average Count': {'experience': 14.0,
                'interesting': 8.0,
                'firm': 13.0,
                'enjoy': 19.0,
                'area': 3.0,
                'what': 12.0,
                'along': 1.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        # The report should be a DataFrame with the correct columns and index
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_3(self):
        # Using the third set of test data
        report = task_func(self.test_data_sets[2])
        expected = pd.DataFrame(
            {'Total Count': {'our': 11.0,
            'then': 2.0,
            'imagine': 6.0,
            'heavy': 17.0,
            'low': 6.0,
            'site': 12.0,
            'nearly': 3.0,
            'organization': 6.0,
            'me': 14.0,
            'eat': 17.0},
            'Average Count': {'our': 11.0,
            'then': 2.0,
            'imagine': 6.0,
            'heavy': 17.0,
            'low': 6.0,
            'site': 12.0,
            'nearly': 3.0,
            'organization': 6.0,
            'me': 14.0,
            'eat': 17.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_4(self):
        # Using the fourth set of test data
        report = task_func(self.test_data_sets[3])
        expected = pd.DataFrame(
            {'Total Count': {'involve': 2.0,
            'money': 11.0,
            'use': 15.0,
            'fish': 19.0,
            'boy': 3.0,
            'both': 10.0},
            'Average Count': {'involve': 2.0,
            'money': 11.0,
            'use': 15.0,
            'fish': 19.0,
            'boy': 3.0,
            'both': 10.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_5(self):
        # Using the fifth set of test data
        report = task_func(self.test_data_sets[4])
        expected = pd.DataFrame(
            {'Total Count': {'take': 18.0, 'activity': 12.0, 'tend': 10.0},
            'Average Count': {'take': 9.0, 'activity': 12.0, 'tend': 10.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)