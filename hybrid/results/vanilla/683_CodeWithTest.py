import math
import yaml

def task_func(yaml_path, key):
    # Read the YAML file
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    # Check if the key exists in the data
    if key in data:
        # Apply the cosine function to the value associated with the key
        data[key] = math.cos(data[key])
    else:
        raise KeyError(f"The key '{key}' does not exist in the YAML data.")
    
    # Write the modified data back to the YAML file
    with open(yaml_path, 'w') as file:
        yaml.safe_dump(data, file)
    
    # Return the modified data
    return data
import unittest
import os
class TestCases(unittest.TestCase):
    def base(self, yaml_path, key, contents, expected):
        # Create YAML file
        with open(yaml_path, 'w') as file:
            yaml.safe_dump(contents, file)
        # Run function
        data = task_func(yaml_path, key)
        # Check data
        self.assertEqual(data, expected)
        # Remove YAML file
        os.remove(yaml_path)
    def test_case_1(self):
        self.base('./data.yaml', 'ele', {'ele': 1, 'ale': 2, 'ile': 3}, {'ele': math.cos(1), 'ale': 2, 'ile': 3})
    def test_case_2(self):
        self.base('./y.yaml', 'zzz', {'zzz': 1, 'yyy': 2, 'xxx': 3}, {'zzz': math.cos(1), 'yyy': 2, 'xxx': 3})
    def test_case_3(self):
        self.base('./data.yaml', 'ale', {'ele': 1, 'ale': 2, 'ile': 3}, {'ele': 1, 'ale': math.cos(2), 'ile': 3})
    def test_case_4(self):
        self.base('./y.yaml', 'yyy', {'zzz': 1, 'yyy': 2, 'xxx': 3}, {'zzz': 1, 'yyy': math.cos(2), 'xxx': 3})
    def test_case_5(self):
        self.base('./data.yaml', 'ile', {'ele': 1, 'ale': 2, 'ile': 3}, {'ele': 1, 'ale': 2, 'ile': math.cos(3)})


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)