import csv
import random

def task_func(csv_file='names.csv', 
              latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
              names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
              encoding='latin-1', rng_seed=None):
    # Validate input types
    if not isinstance(csv_file, str):
        raise TypeError("csv_file must be a string.")
    if not isinstance(latin_names, list):
        raise TypeError("latin_names must be a list.")
    if not isinstance(names, list):
        raise TypeError("names must be a list.")
    
    # Set the random seed if provided
    if rng_seed is not None:
        random.seed(rng_seed)
    
    # Determine the total number of entries
    total_entries = 100
    half_entries = total_entries // 2
    
    # Generate random names and ages
    data = []
    for _ in range(half_entries):
        if latin_names:
            name = random.choice(latin_names)
        else:
            name = ''
        age = random.randint(20, 50)
        data.append([name, age])
    
    for _ in range(half_entries):
        if names:
            name = random.choice(names)
        else:
            name = ''
        age = random.randint(20, 50)
        data.append([name, age])
    
    # Write to CSV file
    with open(csv_file, 'w', newline='', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerows(data)
    
    return csv_file
import unittest
import os
import csv
from faker import Faker
from pathlib import Path
class TestCases(unittest.TestCase):
    def test_case_1(self):
        'default params'
        latin_names = ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']
        names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']
        file_name = task_func(rng_seed=1)
        self.assertEqual(file_name, 'names.csv')
        self.assertTrue(os.path.isfile(file_name))
        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)
        # remove file
        Path(file_name).unlink()
    def test_rng(self):
        'test rng reproducability'
        file_name1 = task_func(csv_file='test1.csv', rng_seed=12)
        file_name2 = task_func(csv_file='test2.csv', rng_seed=12)
        self.assertEqual(file_name1, 'test1.csv')
        self.assertEqual(file_name2, 'test2.csv')
        self.assertTrue(os.path.isfile(file_name1))
        self.assertTrue(os.path.isfile(file_name2))
        with open(file_name1, 'r', newline='', encoding='latin-1') as file1:
            with open(file_name2, 'r', newline='', encoding='latin-1') as file2:
                reader1 = csv.reader(file1)
                rows1 = list(reader1)
                reader2 = csv.reader(file2)
                rows2 = list(reader2)
                self.assertEqual(rows1, rows2)
        # remove files
        Path(file_name1).unlink()
        Path(file_name2).unlink()
    def test_case_2(self):
        'different encoding'
        custom_file = 'custom_names.csv'
        latin_names = ['Méndez']
        names = ['Simon']
        file_name = task_func(csv_file=custom_file, names=names, encoding='utf-8',
                          latin_names=latin_names, rng_seed=1)
        self.assertEqual(file_name, custom_file)
        self.assertTrue(os.path.isfile(custom_file))
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)
        # remove file
        Path(file_name).unlink()
    def test_case_3(self):
        latin_names = [Faker().first_name() for _ in range(5)]
        names = [Faker().first_name() for _ in range(5)]
        file_name = task_func(latin_names=latin_names, names=names, rng_seed=1)
        self.assertEqual(file_name, file_name)
        self.assertTrue(os.path.isfile(file_name))
        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)
            self.assertEqual(rows[0], ['Name', 'Age'])
            csv_names = [row[0] for row in rows[1:]]
            for name in csv_names:
                self.assertIn(name, latin_names+names)
            ages = [int(row[1]) for row in rows[1:]]
            for age in ages:
                self.assertTrue(20 <= age <= 50)
        # remove file
        Path(file_name).unlink()
    def test_case_4(self):
        'emtpy name lists'
        file_name = task_func(latin_names=[], names=[], rng_seed=1)
        self.assertEqual(file_name, file_name)
        self.assertTrue(os.path.isfile(file_name))
        with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0], ['Name', 'Age'])
        # remove file
        Path(file_name).unlink()
    def test_case_5(self):
        'edge cases'
        self.assertRaises(Exception, task_func, {'csv_file': 1, 'rng_seed': 12})
        self.assertRaises(Exception, task_func, {'latin_names': 'test', 'rng_seed': 12})
        self.assertRaises(Exception, task_func, {'names': 24, 'rng_seed': 12})
        # remove file if generated
        if os.path.isfile('names.csv'):
            Path('names.csv').unlink()


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)