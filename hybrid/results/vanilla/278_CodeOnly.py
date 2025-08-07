import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random coefficients a, b, and c between -10 and 10
    a = np.random.randint(-10, 11)
    b = np.random.randint(-10, 11)
    c = np.random.randint(-10, 11)
    
    # Ensure a is not zero to maintain the quadratic nature
    while a == 0:
        a = np.random.randint(-10, 11)
    
    # Define the variable and the quadratic equation
    x = symbols('x')
    equation = a * x**2 + b * x + c
    
    # Solve the quadratic equation
    solutions = solve(equation, x)
    
    # Round the solutions to the specified precision
    rounded_solutions = tuple(
        complex(round(sol.evalf().as_real_imag()[0], precision), 
                round(sol.evalf().as_real_imag()[1], precision))
        for sol in solutions
    )
    
    return rounded_solutions

# Example usage
print(task_func(precision=2, seed=0))