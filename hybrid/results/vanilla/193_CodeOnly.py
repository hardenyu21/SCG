import pandas as pd
import numpy as np
from random import choice, randint, sample

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

def generate_random_data(data_type):
    if data_type == str:
        return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    elif data_type == int:
        return randint(0, 9)
    elif data_type == float:
        return float(randint(0, 9))
    elif data_type == list:
        return [randint(0, 9) for _ in range(randint(1, 5))]
    elif data_type == tuple:
        return tuple(randint(0, 9) for _ in range(randint(1, 5)))
    elif data_type == dict:
        return {randint(0, 9): randint(0, 9) for _ in range(randint(1, 5))}
    elif data_type == set:
        return set(sample(range(10), randint(1, 5)))

def task_func(rows, columns):
    data = {f'col{i}': [generate_random_data(choice(DATA_TYPES)) for _ in range(rows)] for i in range(columns)}
    return pd.DataFrame(data)

# Example usage:
# df = task_func(10, 5)
# print(df)