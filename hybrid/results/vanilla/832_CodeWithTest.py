import pickle
import os

def task_func(filename, data):
    try:
        # Extract the directory from the filename
        directory = os.path.dirname(filename)
        
        # Check if the directory exists, create it if it doesn't
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Serialize the data using pickle and write it to the file
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        
        return True
    except Exception as e:
        # Print the exception for debugging purposes
        print(f"An error occurred: {e}")
        return False
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_data = {'key': 'value'}
        self.filename = 'test_file.pkl'
    def tearDown(self):
        # Remove the file after the test
        if os.path.exists(self.filename):
            os.remove(self.filename)
    def test_serialization_success(self):
        # Test successful serialization
        self.assertTrue(task_func(self.filename, self.test_data))
        # Verify the file exists
        self.assertTrue(os.path.exists(self.filename))
    def test_serialization_readback(self):
        # Test if the serialized then deserialized data matches the original data
        task_func(self.filename, self.test_data)
        with open(self.filename, 'rb') as f:
            data_readback = pickle.load(f)
        self.assertEqual(self.test_data, data_readback)
    def test_serialization_failure(self):
        # Test failure due to an invalid filename (e.g., directory does not exist)
        result = task_func('/non/existent/path/' + self.filename, self.test_data)
        self.assertFalse(result)
import unittest


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)