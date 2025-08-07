def task_func(x, w):
    max_weight = float('-inf')
    max_substr = ""
    
    # Iterate over all possible starting points of substrings
    for start in range(len(x)):
        current_weight = 0
        current_substr = ""
        
        # Iterate over all possible ending points of substrings starting from 'start'
        for end in range(start, len(x)):
            current_char = x[end]
            current_weight += w.get(current_char, 0)
            current_substr += current_char
            
            # Update max_weight and max_substr if the current substring has a higher weight
            if current_weight > max_weight:
                max_weight = current_weight
                max_substr = current_substr
    
    return max_substr

# Example usage:
x = "abcde"
w = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(task_func(x, w))  # Output: "abcde"