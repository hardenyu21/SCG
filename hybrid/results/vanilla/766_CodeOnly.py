import re
import collections

def task_func(string, patterns=['nnn', 'aaa', 'sss', 'ddd', 'fff']):
    # Check if the input string is a string
    if not isinstance(string, str):
        raise TypeError("The input string must be a str.")
    
    # Check if patterns is a list of strings
    if not isinstance(patterns, list) or not all(isinstance(pattern, str) for pattern in patterns):
        raise TypeError("Patterns must be a list of str.")
    
    # Initialize a dictionary to store the counts of each pattern
    pattern_counts = collections.defaultdict(int)
    
    # Iterate over each pattern and count its occurrences in the string
    for pattern in patterns:
        # Use re.findall to find all non-overlapping occurrences of the pattern
        matches = re.findall(pattern, string)
        # Update the count for the current pattern
        pattern_counts[pattern] = len(matches)
    
    # Convert defaultdict to a regular dict before returning
    return dict(pattern_counts)