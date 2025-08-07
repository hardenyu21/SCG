import random
import matplotlib.pyplot as plt

# Constants
SALARY_RANGE = (20000, 100000)

def task_func(dict1):
    # Extract the number of employees in the department with code 'EMPXX'
    num_employees = dict1.get('EMPXX', 0)
    
    # Generate random salaries for each employee
    salaries = [random.uniform(*SALARY_RANGE) for _ in range(num_employees)]
    
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=10, edgecolor='black')
    
    # Set the title and labels
    ax.set_title('Salary Distribution in EMPXX Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax
import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        random.seed(42)
        d = {'EMPXX': 10, 'MANXX': 5, 'DEVXX': 8, 'HRXX': 7}
        ax = task_func(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')
    def test_case_2(self):
        random.seed(42)
        d = {'EMPXX': 5, 'MANXX': 2, 'DEVXX': 3, 'HRXX': 4}
        ax = task_func(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')
    def test_case_3(self):
        random.seed(42)
        d = {'EMPXX': 3, 'MANXX': 1, 'DEVXX': 1, 'HRXX': 7}
        ax = task_func(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')
    def test_case_4(self):
        random.seed(42)
        d = {'EMPXX': 6, 'MANXX': 7, 'DEVXX': 2, 'HRXX': 1}
        ax = task_func(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')
    def test_case_5(self):
        random.seed(42)
        d = {'EMPXX': 1, 'MANXX': 1, 'DEVXX': 1, 'HRXX': 1}
        ax = task_func(d)
        self.assertEqual(ax.get_title(), 'Salary Distribution in EMPXX Department')
        self.assertEqual(ax.get_xlabel(), 'Salary')
        self.assertEqual(ax.get_ylabel(), 'Number of Employees')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)