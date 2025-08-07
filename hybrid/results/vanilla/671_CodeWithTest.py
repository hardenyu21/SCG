import os
import random
import json

def task_func(directory, n):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(n):
        # Generate a random integer between 1 and 100
        random_number = random.randint(1, 100)
        
        # Create a JSON object with the key 'number'
        json_content = {'number': random_number}
        
        # Convert the JSON object to a string
        json_string = json.dumps(json_content)
        
        # Define the file path
        file_path = os.path.join(directory, f'file_{i+1}.json')
        
        # Write the JSON content to the file
        with open(file_path, 'w+') as file:
            file.write(json_string)
            # Reset the cursor to the beginning of the file
            file.seek(0)
    
    # Output the directory where the files were generated
    return directory
import unittest
import shutil
class TestCases(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree('./source', ignore_errors=True)
        shutil.rmtree('./src', ignore_errors=True)
        shutil.rmtree('./s', ignore_errors=True)
    def test_case_1(self):
        random.seed(0)
        directory = task_func('./source', 10)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in sorted(os.listdir(directory)):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 50}, {'number': 98}, {'number': 54}, {'number': 6}, {'number': 34}, {'number': 66}, {'number': 63}, {'number': 52}, {'number': 39}, {'number': 62}])
        shutil.rmtree(directory)
    def test_case_2(self):
        random.seed(1)
        directory = task_func('./src', 1)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 18}])
        shutil.rmtree(directory)
    def test_case_3(self):
        directory = task_func('./s', 100)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 100)
        shutil.rmtree(directory)
    def test_case_4(self):
        directory = task_func('./s', 0)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 0)
        shutil.rmtree(directory)
    def test_case_5(self):
        random.seed(2)
        directory = task_func('./source', 1)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 8}])
        shutil.rmtree(directory)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)