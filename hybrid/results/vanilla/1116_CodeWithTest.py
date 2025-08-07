import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def task_func(dict1):
    # Extract employee names from the department "EMP$$"
    employees = [name for name, dept in dict1.items() if dept == "EMP$$"]
    
    # Generate random ages for each employee within the specified range
    ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for _ in employees]
    
    # Calculate mean
    mean_age = statistics.mean(ages)
    
    # Calculate median
    median_age = statistics.median(ages)
    
    # Calculate mode(s)
    try:
        mode_ages = statistics.mode(ages)
        mode_ages = [mode_ages]  # Convert to list for consistency
    except statistics.StatisticsError:
        # If there is no unique mode, calculate all modes
        mode_ages = statistics.multimode(ages)
    
    # Return the results as a tuple
    return (mean_age, median_age, mode_ages)

# Example usage:
# employee_dict = {
#     "Alice": "EMP$$",
#     "Bob": "HR",
#     "Charlie": "EMP$$",
#     "David": "EMP$$",
#     "Eve": "Marketing"
# }
# print(task_func(employee_dict))
import unittest
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(0)
        # Input: 10 employees in "EMP$$" department
        d = {'EMP$$': 10}
        mean_age, median_age, mode_age = task_func(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_2(self):
        random.seed(0)
        # Input: Different number of employees in multiple departments
        d = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = task_func(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_3(self):
        random.seed(0)
        # Input: No employees in "EMP$$" department
        d = {'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = task_func(d)
        
        # Checks
        self.assertEqual(mean_age, 0)
        self.assertEqual(median_age, 0)
        self.assertEqual(mode_age, [])
    
    def test_case_4(self):
        random.seed(0)
        # Input: Large number of employees in "EMP$$" department to increase likelihood of multiple modes
        d = {'EMP$$': 1000}
        mean_age, median_age, mode_age = task_func(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_5(self):
        random.seed(0)
        # Input: Only one employee in "EMP$$" department
        d = {'EMP$$': 1}
        mean_age, median_age, mode_age = task_func(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertEqual(mean_age, median_age)
        self.assertEqual([mean_age], mode_age)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)