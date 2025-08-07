import itertools
from typing import Any
from scipy import stats

def task_func(input_list: list, repetitions: int) -> Any:
    # Repeat the input list the specified number of times
    repeated_list = list(itertools.chain.from_iterable(itertools.repeat(input_list, repetitions)))
    
    # Calculate the mode of the flattened list
    mode_result = stats.mode(repeated_list)
    
    return mode_result

# Example usage:
# result = task_func([1, 2, 3], 5)
# print(result)