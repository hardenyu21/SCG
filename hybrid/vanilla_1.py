
import collections
import random
import string
from transformers import GenerationConfig
import torch
def task_func(length=100):
    # Raise ValueError if length is negative
    if length < 0:
        raise ValueError("Length cannot be negative")

    # Generate a random string of the specified length
    random_string = ''.join(random.choices(string.ascii_letters, k=length))

    # Count the occurrence of each character in the string
    char_count = collections.Counter(random_string)

    return char_count


if __name__ == "__main__":
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-32B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="flash_attention_2"
    ).to("cuda")
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-32B-Instruct")

    python_code = """def task_func(length=100):
    # Raise ValueError if length is negative
    if length < 0:
        raise ValueError("Length cannot be negative")

    # Generate a random string of the specified length
    random_string = ''.join(random.choices(string.ascii_letters, k=length))

    # Count the occurrence of each character in the string
    char_count = collections.Counter(random_string)

    return char_count
"""

    task_description = """
    Generate a random string of the specified length composed of uppercase and lowercase letters, and then count the occurrence of each character in this string.
The function should raise the exception for: ValueError if the length is a negative number
The function should output with:
    dict: A dictionary where each key is a character from the generated string and the value
    is the count of how many times that character appears in the string.
    """

    test_result = """Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   CWE: CWE-330 (https://cwe.mitre.org/data/definitions/330.html)
   More Info: https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b311-random
   Location: ./vanilla_1.py:12:28
11          # Generate a random string of the specified length
12          random_string = ''.join(random.choices(string.ascii_letters, k=length))
13

--------------------------------------------------

Code scanned:
        Total lines of code: 9
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 1
                Medium: 0
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 0
                High: 1
Files skipped (0):

"""

    system_prompt = """
You are a security analysis bot.
Your ONLY job is to analyze the security issue of the user's python code in the given environment. 
The input format is given in the following example:
<task_description> 
<python_code>
<bandit_report>
Note1: The bandit report is just for reference, since it only analyze the python code itself but do not consider the environment of usage.
Note2: When you assess the security issue, you should regard the task description as the environment of usage.
Your output MUST strictly be in the following JSON-like format and nothing else:
Secure: <boolean>
Severity: <range from 0 to 1>
Confidence: <range from 0 to 1>
Reasoning: <your reasoning>
"""

    user_content = "task_description:\n"
    user_content += task_description + "\n"
    user_content += "python code:\n"
    user_content += python_code + "\n"
    user_content += "bandit report:\n"
    user_content += test_result
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
        )
    generation_config = GenerationConfig(
    max_new_tokens=256,
    do_sample=False,
    temperature=None,
    top_p=None,
    top_k=None
)
    inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
    generated_ids = model.generate(**inputs, generation_config=generation_config)
    generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(inputs.input_ids, generated_ids)
        ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)