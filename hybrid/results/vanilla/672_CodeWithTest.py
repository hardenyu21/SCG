import csv
import sys

def task_func(filename):
    # Read the CSV file and store the lines
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)
    
    # Reverse the order of the lines
    lines.reverse()
    
    # Write the reversed lines back to the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    
    # Reset the cursor to the beginning of the file
    with open(filename, mode='r+', newline='') as file:
        file.seek(0)

# Example usage:
# task_func('example.csv')
import unittest
import os
class TestCases(unittest.TestCase):
    def base(self, filename, contents, expected):
        # Create file
        with open(filename, 'w') as file:
            file.write(contents)
        # Run function
        task_func(filename)
        # Check file
        with open(filename, 'r') as file:
            txt = file.read()
            self.assertEqual(txt, expected)
        # Remove file
        os.remove(filename)
    def test_case_1(self):
        self.base('file.csv', "a,b\nc,d\ne,f\ng,h\n", "g,h\ne,f\nc,d\na,b\n")
    
    def test_case_2(self):
        self.base('file.csv', "a,b,c\nd,e,f\ng,h,i\n", "g,h,i\nd,e,f\na,b,c\n")
    def test_case_3(self):
        self.base('file.csv', "a,b,c,d\ne,f,g,h\ni,j,k,l\n", "i,j,k,l\ne,f,g,h\na,b,c,d\n")
    
    def test_case_4(self):
        self.base('file.csv', "a,b,c,d,e\nf,g,h,i,j\nk,l,m,n,o\n", "k,l,m,n,o\nf,g,h,i,j\na,b,c,d,e\n")
    def test_case_5(self):
        self.base('file.csv', "a,b,c,d,e,f\ng,h,i,j,k,l\nm,n,o,p,q,r\n", "m,n,o,p,q,r\ng,h,i,j,k,l\na,b,c,d,e,f\n")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)