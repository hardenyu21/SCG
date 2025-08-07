import urllib.request
import zipfile
import os
import urllib.error

def task_func(
    url: str,
    save_path: str = "downloaded_file.zip",
    extract_path: str = "extracted_files",
) -> str:
    try:
        # Download the ZIP file from the specified URL
        urllib.request.urlretrieve(url, save_path)
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Download Error: {str(e)}"

    try:
        # Create the directory for extraction if it doesn't exist
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        # Extract the ZIP file
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
    except zipfile.BadZipFile:
        return "Error: The downloaded file is not a valid ZIP file."
    except Exception as e:
        return f"Extraction Error: {str(e)}"

    try:
        # Delete the downloaded ZIP file
        os.remove(save_path)
    except Exception as e:
        return f"Cleanup Error: {str(e)}"

    # Return the path to the extracted files
    return extract_path