import difflib
import gzip

def task_func(file_path1, file_path2):
    # Read the contents of the first gzip file
    with gzip.open(file_path1, 'rt', encoding='utf-8') as f1:
        content1 = f1.readlines()
    
    # Read the contents of the second gzip file
    with gzip.open(file_path2, 'rt', encoding='utf-8') as f2:
        content2 = f2.readlines()
    
    # Use difflib to compute the differences
    diff = difflib.unified_diff(content1, content2, fromfile=file_path1, tofile=file_path2, lineterm='')
    
    # Join the differences into a single string
    diff_str = '\n'.join(diff)
    
    return diff_str