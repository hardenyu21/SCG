import subprocess
import threading

def task_func(file_list):
    def run_file(file, results, index):
        try:
            result = subprocess.run(['python', file], capture_output=True, text=True)
            results[index] = result.returncode
        except Exception as e:
            results[index] = -1  # Indicate an error occurred

    threads = []
    results = [None] * len(file_list)

    for i, file in enumerate(file_list):
        thread = threading.Thread(target=run_file, args=(file, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# Example usage:
# file_list = ['script1.py', 'script2.py', 'script3.py']
# exit_codes = task_func(file_list)
# print(exit_codes)