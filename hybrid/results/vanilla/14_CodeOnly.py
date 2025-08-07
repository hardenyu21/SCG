import configparser
import os
import shutil

def task_func(config_file_path, archive_dir='/home/user/archive'):
    # Check if the config file exists
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"The configuration file '{config_file_path}' does not exist.")
    
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    
    # Check if the 'Project' section and 'directory' key exist
    if 'Project' not in config or 'directory' not in config['Project']:
        raise Exception("The configuration file is missing the 'Project' section or 'directory' key.")
    
    # Get the project directory from the configuration
    project_directory = config['Project']['directory']
    
    # Check if the project directory exists
    if not os.path.exists(project_directory):
        raise FileNotFoundError(f"The project directory '{project_directory}' does not exist.")
    
    # Get the basename of the project directory
    project_basename = os.path.basename(project_directory)
    
    # Construct the path for the ZIP archive
    zip_file_path = os.path.join(archive_dir, f"{project_basename}.zip")
    
    # Create the archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # Try to create the ZIP archive
    try:
        shutil.make_archive(os.path.join(archive_dir, project_basename), 'zip', project_directory)
    except Exception as e:
        raise Exception(f"Failed to create the ZIP archive: {e}")
    
    return True