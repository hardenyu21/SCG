import shutil
import pathlib

def task_func(source_path, destination_path):
    # Convert paths to pathlib.Path objects
    source_path = pathlib.Path(source_path)
    destination_path = pathlib.Path(destination_path)
    
    # Check if source_path exists and is a directory
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("source_path does not exist or is not a directory.")
    
    # Ensure destination_path exists, create if it doesn't
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # List files in the source directory without descending into subdirectories
    files_copied = []
    for item in source_path.iterdir():
        if item.is_file():
            # Copy the file to the destination directory
            shutil.copy(item, destination_path)
            # Append the filename to the list
            files_copied.append(item.name)
    
    # Return the source directory name and the list of copied filenames
    return (source_path.name, files_copied)
import unittest
import tempfile
import pathlib
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_source_dir = pathlib.Path(self.temp_dir.name) / "testf817-source"
        self.test_target_dir = pathlib.Path(self.temp_dir.name) / "testf817-target"
        self.test_source_dir.mkdir(parents=True, exist_ok=True)
        self.test_target_dir.mkdir(parents=True, exist_ok=True)
    def tearDown(self):
        self.temp_dir.cleanup()
    def create_files(self, paths):
        for path in paths:
            full_path = self.test_source_dir / path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.touch()
    def test_case_1(self):
        # Test empty directory
        target_dir_before = list(self.test_target_dir.iterdir())
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        target_dir_after = list(self.test_target_dir.iterdir())
        self.assertEqual(result, ("testf817-source", []))
        self.assertEqual(target_dir_before, target_dir_after)
    def test_case_2(self):
        # Test directory with one file
        self.create_files(["file1.txt"])
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(result, ("testf817-source", ["file1.txt"]))
        # Check if files are copied correctly
        self.assertEqual(
            list(self.test_target_dir.iterdir()), [self.test_target_dir / "file1.txt"]
        )
    def test_case_3(self):
        # Test directory with multiple files
        self.create_files(["file1.txt", "file2.txt", "file3.txt"])
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "testf817-source")
        self.assertEqual(
            sorted(result[1]), sorted(["file1.txt", "file2.txt", "file3.txt"])
        )
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [
                    self.test_target_dir / "file1.txt",
                    self.test_target_dir / "file2.txt",
                    self.test_target_dir / "file3.txt",
                ]
            ),
        )
    def test_case_4(self):
        # Test directory with subdirectories
        self.test_source_dir.joinpath("subdir1").mkdir()
        self.create_files(["file1.txt", "file2.txt"])
        self.create_files(["subdir1/file3.txt"])  # File inside subdirectory
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "testf817-source")
        self.assertEqual(sorted(result[1]), sorted(["file1.txt", "file2.txt"]))
        # Check if files in subdirectories are ignored and only files in the source directory are copied
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [self.test_target_dir / "file1.txt", self.test_target_dir / "file2.txt"]
            ),
        )
    def test_case_5(self):
        # Test non-existent source directory
        with self.assertRaises(ValueError):
            task_func(str(self.test_source_dir / "nonexistent"), str(self.test_target_dir))
    def test_case_6(self):
        # Test non-existent destination directory
        shutil.rmtree(self.test_target_dir)
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(result, ("testf817-source", []))
        # Check if destination directory is created
        self.assertTrue(self.test_target_dir.exists())
    def test_case_7(self):
        # Test copying files to existing destination directory
        self.create_files(["file1.txt", "file2.txt"])
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        self.assertEqual(sorted(result[1]), sorted(["file1.txt", "file2.txt"]))
        # Call the function again
        self.create_files(["file3.txt", "file4.txt"])
        result = task_func(str(self.test_source_dir), str(self.test_target_dir))
        # There should now be 4 files in the directory
        self.assertEqual(
            sorted(self.test_source_dir.iterdir()),
            sorted(
                [
                    self.test_source_dir / "file1.txt",
                    self.test_source_dir / "file2.txt",
                    self.test_source_dir / "file3.txt",
                    self.test_source_dir / "file4.txt",
                ]
            ),
        )
        # which means 4 files should have been copied
        self.assertEqual(
            sorted(result[1]),
            sorted(["file1.txt", "file2.txt", "file3.txt", "file4.txt"]),
        )
        # and 4 files should be in the destination
        self.assertEqual(
            sorted(self.test_target_dir.iterdir()),
            sorted(
                [
                    self.test_target_dir / "file1.txt",
                    self.test_target_dir / "file2.txt",
                    self.test_target_dir / "file3.txt",
                    self.test_target_dir / "file4.txt",
                ]
            ),
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)