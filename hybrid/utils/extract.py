import os
from typing import Union
import re
def extract_py_from_output(text: str) -> str:
    """
    Safely extracts Python code blocks from text containing markdown-style code snippets.
    Format: ```python ... ```
    
    Args:
        text: Input text potentially containing code blocks
        
    Returns:
        Extracted Python code as string, or empty string if not found
    """
    start_marker = "```python"
    end_markers = ["```", "# Example usage"]
    
    # Find start marker with case-insensitive fallback
    start_idx = text.find(start_marker)
    if start_idx == -1:
        # Handle case variations (Python, PYTHON, etc.)
        lower_text = text.lower()
        lower_marker = start_marker.lower()
        start_idx = lower_text.find(lower_marker)
        if start_idx == -1:
            return ""
    
    # Calculate search start position after the start marker
    search_start = start_idx + len(start_marker)
    
    # Find end marker AFTER the start marker position
    for end_marker in end_markers:
        end_idx = text.find(end_marker, search_start)
        if end_idx != -1:
            break
    
    if end_idx == -1:
        return ""
    
    # Extract raw code content
    code = text[search_start:end_idx]
    lines = code.splitlines()

    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    
    return "\n".join(lines)

def read_unit_test(raw_data: dict) -> str:
    """
    Read unittest from text
    """
    return raw_data['test']


def construct_test_code(code: str, test: str) -> str:
    """
    Combine the code, unittests and test harness.
    """
    test_harness = """\n
# --- Unittest Harness ---
import unittest
import sys

# Load all tests from the current execution scope
suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])

# Run the tests with a quiet runner
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)

# The final expression evaluates to True or False, serving as the script's result
result.wasSuccessful()"""
    return f"{code}\n\n{test}\n\n{test_harness}"

def construct_evaluation_prompt(task_description: str, code: str, bandit_report: str) -> str:
    """
    Combine task description, code, and bandit report into a single string.
    """
    prompt = f"<task_description>\n{task_description}"
    prompt += f"\n<python_code>\n{code}"
    prompt += f"\n<bandit_report>\n{bandit_report}"
    return prompt


def parse_security_evaluation_result(report_string: str) -> dict | None:
    """
    Parses a security report string with a custom format into a dictionary.

    The expected format is:
    Secure: <boolean>
    Severity: <range from 0 to 1>
    Confidence: <range from 0 to 1>
    Reasoning: <your reasoning>

    Args:
        report_string: The string output from the language model.

    Returns:
        A dictionary containing the parsed data with correct types,
        or None if the string does not match the expected format.
    """

    pattern = re.compile(
        r"Secure:\s*(?P<secure>True|False|true|false)\s*"
        r"Severity:\s*(?P<severity>[\d\.]+)\s*"
        r"Confidence:\s*(?P<confidence>[\d\.]+)\s*"
        r"Reasoning:\s*(?P<reasoning>.*)",
        re.DOTALL | re.IGNORECASE
    )

    match = pattern.search(report_string)

    if not match:
        return None

    data = match.groupdict()

    try:
        parsed_dict = {
            "Secure": data['secure'].lower() == 'true',
            "Severity": float(data['severity']),
            "Confidence": float(data['confidence']),
            "Reasoning": data['reasoning'].strip()
        }
        return parsed_dict
    except (ValueError, TypeError) as e:
        print(f"Error converting types: {e}")
        return None

def save_code_to_file(code_string: Union[str, list[str]], filepath: str) -> bool:
    """
    Saves the given code string to the specified file path.

    Args:
        code_string: The code content to be saved.
        filepath: The full file path (e.g., 'output/tests/test_new.py').
    """
    try:
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if isinstance(code_string, list):
            with open(filepath, 'w', encoding='utf-8') as f:
                for code in code_string:
                    f.write(code)
                    f.write("\n\n\n")
        elif isinstance(code_string, str):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code_string)

    except Exception as e:
        print(f"A critical error occurred for '{filepath}': {e}")


if __name__ == "__main__":

    pass