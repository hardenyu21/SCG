import collections
import operator
import os
import shutil

def task_func(data_dict, source_directory, backup_directory):
    # Task 1: Update the dictionary by adding a key 'a' with the value 1
    data_dict['a'] = 1

    # Task 2: Sort the dictionary by the frequency of its values in descending order
    value_counter = collections.Counter(data_dict.values())
    sorted_value_frequencies = sorted(value_counter.items(), key=operator.itemgetter(1), reverse=True)

    # Task 3: Back up all files from the specified source directory to a backup directory
    try:
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)
        for filename in os.listdir(source_directory):
            source_file = os.path.join(source_directory, filename)
            backup_file = os.path.join(backup_directory, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, backup_file)
        backup_status = True
    except Exception as e:
        print(f"An error occurred during backup: {e}")
        backup_status = False

    return data_dict, sorted_value_frequencies, backup_status