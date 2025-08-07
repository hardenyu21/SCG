from collections import Counter
import logging

def task_func(letter_list, element, log_path):
    # Configure logging
    log_file = f"{log_path}/task_func.log"
    logging.basicConfig(
        filename=log_file,
        filemode='w',  # Overwrite the log file if it exists
        level=logging.DEBUG,
        format='%(levelname)s:%(message)s',
        encoding='utf-8'
    )
    
    # Log function call
    logging.info(f"Function called with list: {letter_list} and element: {element}")
    
    # Check if the element is in the letter list
    if element not in letter_list:
        logging.error("The element is not in the letter list.")
        logging.shutdown()
        raise ValueError("The element is not in the letter list.")
    
    # Count the frequency of the element
    element_frequency = Counter(letter_list)[element]
    
    # Log the frequency
    logging.info(f"Frequency of '{element}' is {element_frequency}")
    
    # Shutdown logging to release file handles
    logging.shutdown()
    
    return element_frequency