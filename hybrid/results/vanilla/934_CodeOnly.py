from collections import Counter
import hashlib

def task_func(word: str) -> dict:
    # Generate adjacent letter pairs
    pairs = [word[i:i+2] for i in range(len(word) - 1)]
    
    # Count occurrences of each pair
    pair_counts = Counter(pairs)
    
    # Convert the dictionary to a string representation
    pair_counts_str = str(pair_counts)
    
    # Encode the string representation as an MD5 hash
    md5_hash = hashlib.md5(pair_counts_str.encode()).hexdigest()
    
    # Return the dictionary of pair counts
    return pair_counts

# Example usage:
# result = task_func("hello")
# print(result)