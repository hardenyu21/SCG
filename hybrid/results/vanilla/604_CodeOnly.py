import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(filepath):
    try:
        # Check if the file exists
        with open(filepath, 'r'):
            pass
    except FileNotFoundError:
        logging.error(f"The specified file '{filepath}' does not exist.")
        raise FileNotFoundError(f"The specified file '{filepath}' does not exist.")

    # Define the compiler command
    compiler_command = ['g++', filepath, '-o', 'output_executable']

    try:
        # Run the compilation process
        subprocess.run(compiler_command, check=True)
        logging.info(f"Compilation of '{filepath}' was successful.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Compilation of '{filepath}' failed with error: {e}")
        raise subprocess.CalledProcessError(returncode=e.returncode, cmd=e.cmd, output=e.output, stderr=e.stderr)

# Example usage:
# task_func('example.cpp')