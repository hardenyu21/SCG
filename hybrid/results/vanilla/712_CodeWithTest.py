import os
import shutil
import glob

def task_func(source_dir, dest_dir, extension):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Construct the search pattern for files with the given extension
    search_pattern = os.path.join(source_dir, f'*.{extension}')
    
    # Find all files matching the pattern
    files_to_move = glob.glob(search_pattern)
    
    # Initialize a counter for the number of files moved
    result = 0
    
    # Move each file to the destination directory
    for file_path in files_to_move:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Construct the destination file path
        dest_file_path = os.path.join(dest_dir, file_name)
        
        # Move the file
        shutil.move(file_path, dest_file_path)
        
        # Increment the counter
        result += 1
    
    # Return the count of files moved
    return result
import unittest
class TestCases(unittest.TestCase):
    def tearDown(self):
        for d in ['./source', './destination', './src', './dst', './s', './d']:
            if os.path.exists(d):
                shutil.rmtree(d)
    def test_case_1(self):
        # Create source directory
        if os.path.exists('./source'):
            shutil.rmtree('./source')
        os.mkdir('./source')
        # Create destination directory
        if os.path.exists('./destination'):
            shutil.rmtree('./destination')
        os.mkdir('./destination')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./source', filename), 'w') as f:
                f.write('test')
        # Run function
        task_func('./source', './destination', 'txt')
        # Check files
        for d in ['./destination', './source']:
            if d == './source':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./source')
        shutil.rmtree('./destination')
    def test_case_2(self):
        # Create source directory
        if os.path.exists('./src'):
            shutil.rmtree('./src')
        os.mkdir('./src')
        # Create destination directory
        if os.path.exists('./dst'):
            shutil.rmtree('./dst')
        os.mkdir('./dst')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./src', filename), 'w') as f:
                f.write('test')
        # Run function
        task_func('./src', './dst', 'txt')
        # Check files
        for d in ['./dst', './src']:
            if d == './src':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./src')
        shutil.rmtree('./dst')
    def test_case_3(self):
        # Create source directory
        if os.path.exists('./s'):
            shutil.rmtree('./s')
        os.mkdir('./s')
        # Create destination directory
        if os.path.exists('./d'):
            shutil.rmtree('./d')
        os.mkdir('./d')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./s', filename), 'w') as f:
                f.write('test')
        # Run function
        task_func('./s', './d', 'txt')
        # Check files
        for d in ['./d', './s']:
            if d == './s':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./s')
        shutil.rmtree('./d')
    def test_case_4(self):
        # Create source directory
        if os.path.exists('./s'):
            shutil.rmtree('./s')
        os.mkdir('./s')
        # Create destination directory
        if os.path.exists('./destination'):
            shutil.rmtree('./destination')
        os.mkdir('./destination')
        # Create files
        for filename in ['bbb.txt', 'a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./s', filename), 'w') as f:
                f.write('test')
        # Run function
        task_func('./s', './destination', 'txt')
        # Check files
        for d in ['./destination', './s']:
            if d == './s':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))  
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
        # Remove files
        shutil.rmtree('./s')
        shutil.rmtree('./destination')
    def test_case_5(self):
        # Create source directory
        if os.path.exists('./source'):
            shutil.rmtree('./source')
        os.mkdir('./source')
        # Create destination directory
        if os.path.exists('./d'):
            shutil.rmtree('./d')
        os.mkdir('./d')
        # Create files
        for filename in ['a.txt', 'b.txt', 'c.docx', 'd.docx', 'e.txt', 'a.pdf', 'a.doc']:
            with open(os.path.join('./source', filename), 'w') as f:
                f.write('xxx')
        # Run function
        task_func('./source', './d', 'docx')
        # Check files
        for d in ['./d', './source']:
            if d == './source':
                self.assertTrue(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertTrue(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertTrue(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))
            else:
                self.assertTrue(os.path.exists(os.path.join(d, 'c.docx')))
                self.assertTrue(os.path.exists(os.path.join(d, 'd.docx')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.pdf')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.doc')))
                self.assertFalse(os.path.exists(os.path.join(d, 'a.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'b.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'e.txt')))
                self.assertFalse(os.path.exists(os.path.join(d, 'f.txt')))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)