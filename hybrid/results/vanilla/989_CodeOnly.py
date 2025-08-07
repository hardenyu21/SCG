import random
import string

def task_func(length: int, predicates: list, seed: int = None):
    if length < 0:
        raise ValueError("The specified length must be non-negative.")
    
    if seed is not None:
        random.seed(seed)
    
    # Define valid predicates
    valid_predicates = {
        'has_upper': lambda s: any(c.isupper() for c in s),
        'has_lower': lambda s: any(c.islower() for c in s),
        'has_digit': lambda s: any(c.isdigit() for c in s),
        'has_punctuation': lambda s: any(c in string.punctuation for c in s),
    }
    
    # Deduplicate predicates
    predicates = list(set(predicates))
    
    # Check for invalid predicates
    for predicate in predicates:
        if predicate not in valid_predicates:
            raise KeyError(f"Predicate '{predicate}' is not recognized.")
    
    # Generate random string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    
    # Evaluate predicates
    result = {predicate: valid_predicates[predicate](random_string) for predicate in predicates}
    
    return random_string, result