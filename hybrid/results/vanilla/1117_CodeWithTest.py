import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def task_func(department_data):
    # Initialize a dictionary to hold the department data
    department_levels = collections.defaultdict(list)
    
    # Iterate over each department code and its corresponding employee count
    for department_code, employee_count in department_data.items():
        # Ensure the department code is valid
        if department_code not in PREFICES:
            raise ValueError(f"Invalid department code: {department_code}")
        
        # Randomly assign employee levels based on the employee count
        for _ in range(employee_count):
            # Randomly choose a level for each employee
            level = random.choice(LEVELS)
            department_levels[department_code].append(level)
    
    # Convert the dictionary to a JSON object
    json_object = json.dumps(department_levels, indent=4)
    
    return json_object

# Example usage
department_data = {
    'EMP$$': 5,
    'MAN$$': 3,
    'DEV$$': 7,
    'HR$$': 2
}

print(task_func(department_data))
import unittest
import collections
import random
import json
# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(0)
        input_data = {'EMP$$': 5, 'MAN$$': 3, 'DEV$$': 4, 'HR$$': 2}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        
        for key, value in input_data.items():
            self.assertIn(key, parsed_output)
            self.assertEqual(len(parsed_output[key]), value)
            for level in parsed_output[key]:
                self.assertIn(level, LEVELS)
    
    def test_case_2(self):
        random.seed(0)
        input_data = {'EMP$$': 10}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 1)
        self.assertEqual(len(parsed_output['EMP$$']), 10)
        for level in parsed_output['EMP$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_3(self):
        random.seed(0)
        input_data = {'MAN$$': 6, 'DEV$$': 7}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 2)
        self.assertEqual(len(parsed_output['MAN$$']), 6)
        self.assertEqual(len(parsed_output['DEV$$']), 7)
        for level in parsed_output['MAN$$']:
            self.assertIn(level, LEVELS)
        for level in parsed_output['DEV$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_4(self):
        random.seed(0)
        input_data = {'HR$$': 3}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 1)
        self.assertEqual(len(parsed_output['HR$$']), 3)
        for level in parsed_output['HR$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_5(self):
        random.seed(0)
        input_data = {}
        output_data = task_func(input_data)
        parsed_output = json.loads(output_data)
        self.assertEqual(len(parsed_output), 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)