from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    # Configure logging
    log_file = f"{log_path}/task_func.log"
    logging.basicConfig(
        filename=log_file,
        filemode='w',  # Overwrite the log file if it exists
        level=logging.DEBUG,
        format='%(levelname)s:%(message)s',
        encoding='utf-8'
    )
    
    # Log function call
    logging.info(f"Function called with list: {letter_list} and element: {element}")
    
    # Check if the element is in the letter list
    if element not in letter_list:
        logging.error("The element is not in the letter list.")
        logging.shutdown()
        raise ValueError("The element is not in the letter list.")
    
    # Count the frequency of the element
    element_frequency = Counter(letter_list)[element]
    
    # Log the frequency
    logging.info(f"Frequency of '{element}' is {element_frequency}")
    
    # Shutdown logging to release file handles
    logging.shutdown()
    
    return element_frequency
import unittest
import os, shutil
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_folder = tempfile.mkdtemp()
    def test_case_1(self):
        result = task_func(['a', 'b', 'a', 'c', 'a'], 'a', self.temp_folder)
        self.assertEqual(result, 3)
        with open(self.temp_folder+'/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['a', 'b', 'a', 'c', 'a'] and element: a" in log.readline())
            self.assertTrue("INFO:Frequency of 'a' is 3" in log.readline())
    def test_case_2(self):
        result = task_func(['x', 'y', 'z'], 'y', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder+'/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['x', 'y', 'z'] and element: y" in log.readline())
            self.assertTrue("INFO:Frequency of 'y' is 1" in log.readline())
    def test_case_3(self):
        result = task_func(['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'], 'r', self.temp_folder)
        self.assertEqual(result, 1)
        with open(self.temp_folder+'/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'] and element: r" in log.readline())
            self.assertTrue("INFO:Frequency of 'r' is 1" in log.readline())
    def test_case_4(self):
        result = task_func(['z', 'z', 'z', 'z'], 'z', self.temp_folder)
        self.assertEqual(result, 4)
        with open(self.temp_folder+'/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['z', 'z', 'z', 'z'] and element: z" in log.readline())
            self.assertTrue("INFO:Frequency of 'z' is 4" in log.readline())
    def test_case_5(self):
        with self.assertRaises(ValueError):
            task_func(['a', 'b', 'c'], 'z', self.temp_folder)
        with open(self.temp_folder+'/task_func.log') as log:
            self.assertTrue("INFO:Function called with list: ['a', 'b', 'c'] and element: z" in log.readline())
            self.assertTrue("ERROR:The element is not in the letter list." in log.readline())


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)