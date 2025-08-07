import csv
import random
from faker import Faker

def task_func(file_path, num_rows, random_seed=None):
    # Validate num_rows
    if not isinstance(num_rows, int) or num_rows < 0:
        raise ValueError("num_rows must be an integer >= 0.")
    
    # Initialize Faker
    fake = Faker()
    if random_seed is not None:
        Faker.seed(random_seed)
        random.seed(random_seed)
    
    # Prepare data
    data = []
    for _ in range(num_rows):
        name = fake.name()
        age = random.randint(20, 60)
        address = fake.address().replace('\n', ', ')
        email = fake.email()
        data.append([name, str(age), address, email])
    
    # Write to CSV
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Address', 'Email'])
        writer.writerows(data)
    
    return file_path
import unittest
import csv
import os
from faker import Faker
import tempfile
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.folder_path = tempfile.mkdtemp()
        self.file_path = os.path.join(self.folder_path, 'test.csv')
    def test_rng(self):
        res_path1 = task_func(os.path.join(self.folder_path, 'test1.csv'), 45, random_seed=42)
        res_path2 = task_func(os.path.join(self.folder_path, 'test2.csv'), 45, random_seed=42)
        with open(res_path1, 'r') as file:
            reader = csv.reader(file)
            rows1 = list(reader)
        with open(res_path2, 'r') as file:
            reader = csv.reader(file)
            rows2 = list(reader)
        self.assertEqual(rows1, rows2)
    def test_case_1(self):
        num_rows = 10
        result_path = task_func(self.file_path, num_rows, random_seed=12)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), num_rows + 1)
        
        expected = [['Name', 'Age', 'Address', 'Email'],
            ['Matthew Estrada',
            '50',
            '7479 Angela Shore, South Michael, MA 28059',
            'johnstonjames@example.net'],
            ['Gabrielle Sullivan',
            '37',
            '83167 Donna Dale, Nicoleside, GA 91836',
            'peterswilliam@example.org'],
            ['Jason Carlson',
            '53',
            '013 Kelly Lake Suite 414, West Michael, NY 75635',
            'anthonycarson@example.com'],
            ['Alexander Lowe',
            '42',
            '183 Christian Harbor, South Joshuastad, PA 83984',
            'palmermicheal@example.com'],
            ['John Benjamin',
            '29',
            '8523 Rhonda Avenue, Rosemouth, HI 32166',
            'masonjohn@example.org'],
            ['Dr. Kathy Johnson',
            '44',
            '138 Burns Knoll Suite 727, Christinaton, KY 43754',
            'nbush@example.net'],
            ['David Vega',
            '20',
            '462 James Mountains, New Ashleyview, WV 05639',
            'freynolds@example.com'],
            ['Lauren Bailey',
            '43',
            '202 Lauren Cliffs Suite 836, Lake Michaelport, KY 90824',
            'hhowell@example.org'],
            ['Mercedes Long',
            '50',
            '5152 Jennifer Inlet Apt. 652, East Tonymouth, NM 24011',
            'contrerasmatthew@example.org'],
            ['Anne Walker', '37', 'USNV Ramirez, FPO AE 90740', 'hphillips@example.org']
        ]
        self.assertEqual(rows, expected)
        os.remove(result_path)
    def test_case_2(self):
        # 0 rows
        num_rows = 0
        result_path = task_func(self.file_path, num_rows)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), num_rows + 1)
        os.remove(result_path)
    def test_case_3(self):
        # large amount of rows
        num_rows = 1000
        result_path = task_func(self.file_path, num_rows)
        self.assertTrue(os.path.exists(result_path))
        df = pd.read_csv(result_path)
        self.assertTrue(df['Age'].between(20, 60, inclusive='both').all())
        self.assertTrue(df.shape == (1000, 4))
        os.remove(result_path)
    def test_case_4(self):
        #negative rows
        self.assertRaises(Exception, task_func, self.file_path, -2)
        self.assertRaises(Exception, task_func, self.file_path, 1.2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)