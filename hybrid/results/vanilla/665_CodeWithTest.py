import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    # Define the patterns to match
    patterns = ['*.txt', '*.docx']
    
    # Iterate over all files in the source directory
    for root, dirs, files in os.walk(src_dir):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                # Construct full file paths
                src_file = os.path.join(root, filename)
                dst_file = os.path.join(dst_dir, filename)
                
                # Copy the file to the destination directory
                shutil.copy2(src_file, dst_file)
    
    # Return the destination directory
    return dst_dir
import unittest
class TestCases(unittest.TestCase):
    def base(self, src_dir, dst_dir):
        if os.path.exists(src_dir):
            shutil.rmtree(src_dir)
        # Create source directory
        os.mkdir(src_dir)
        # Create destination directory
        os.mkdir(dst_dir)
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join(src_dir, filename), 'w') as f:
                f.write('test')
        # Run function
        task_func(src_dir, dst_dir)
        # Check files
        for d in [src_dir, dst_dir]:
            self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
            self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))
            self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
            self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
            if d == src_dir:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
            else:
                self.assertFalse(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.doc')))
    
    def tearDown(self):
        for d in ['./source', './destination', './src', './dst', './s', './d']:
            if os.path.exists(d):
                shutil.rmtree(d)
    def test_case_1(self):
        self.base('./source', './destination')
    
    def test_case_2(self):
        self.base('./src', './dst')
    
    def test_case_3(self):
        self.base('./s', './d')
    
    def test_case_4(self):
        self.base('./s', './destination')
    def test_case_5(self):
        self.base('./source', './d')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)