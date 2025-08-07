import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    # Find all .docx files in the provided directory
    docx_files = glob.glob(f"{directory_path}/*.docx")
    files_processed = 0

    for file_path in docx_files:
        # Open the document
        doc = Document(file_path)
        modified = False

        # Iterate through each paragraph in the document
        for para in doc.paragraphs:
            # Find all double quotes in the paragraph text
            if '"' in para.text:
                # Replace each double quote with a backslash-escaped double quote
                new_text = para.text.replace('"', '\\"')
                para.text = new_text
                modified = True

        # If any changes were made, save the document
        if modified:
            doc.save(file_path)
            files_processed += 1

    return files_processed