from datasets import load_dataset
import jsonlines, json
from utils.load import load_dataset_by_name
from openai import OpenAI
from utils.config import unittest_generation_system_prompt

def construct_prompt(data):


    total_description = data['task_description']

    description = total_description['description']
    function_name = total_description['function_name']
    function_args = total_description['arguments']
    function_return = total_description['return']
    exception_raise = total_description['raise']
    context = total_description['context']
    security_policy = total_description['security_policy']

    instruct_prompt = description

    detail = "Here are some details of this coding task:\n"
    name = f"1.The function name is: {function_name}\n"
    args = f"2.The arguments are:\n {function_args}\n"
    returns = f"3.The function returns:\n {function_return}\n"
    raises = f"4.Exception raise:\n {exception_raise}\n"
    context = f"5.The contexts are:\n {context}\n"
    import_lib = f"6.You should import the necessary library or package at the begining of your code.\n"
    security = f"7.The security policy you should follow:\n {security_policy}\n"

    
    instruct_prompt = instruct_prompt + detail + name + args + returns + raises + context + import_lib + security
    instruct_prompt_wo_security = instruct_prompt + detail + name + args + returns + raises + context + import_lib
    return instruct_prompt, instruct_prompt_wo_security

def construct_ground_truth(data):
    ground_truth = data['ground_truth']['code_before'] 
    ground_truth += data['ground_truth']['patched_code']
    ground_truth += data['ground_truth']['code_after']
    return ground_truth

def construct_user_content(data):

    user_content = unittest_generation_system_prompt
    user_content += "\nNow This is the code snippet you need to generate unit test for:\n"
    user_content += "<task_description>\n"
    user_content += data['instruct_prompt']
    user_content += "</task_description>\n"
    user_content += "<code>\n"
    user_content += data['canonical_solution']
    user_content += "</code>\n"
    user_content += "Note that you should only output the unit test code, do not include the input code snippet."
    return user_content


def parse_json_from_model_output(raw_output: str) -> dict | None:
    """
    Finds and parses a JSON object from a raw string returned by an LLM.
    Handles extraneous text before or after the JSON object.
    """
    try:
        # Find the starting and ending curly braces of the JSON object
        start_index = raw_output.find('{')
        end_index = raw_output.rfind('}')

        if start_index == -1 or end_index == -1 or end_index < start_index:
            print("Error: Could not find a valid JSON object in the output.")
            return raw_output

        # Extract the JSON part of the string
        json_string = raw_output[start_index : end_index + 1]

        # Parse the extracted string into a Python dictionary
        return json.loads(json_string)

    except json.JSONDecodeError as e:

        return raw_output
    
    except Exception as e:
        print(f"An unexpected error occurred during parsing: {e}")
        return raw_output


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_idx', type=int, default=99)
    args = parser.parse_args()

    count = 0

    client = OpenAI(api_key="", 
                    base_url="https://aigc-api.hkust-gz.edu.cn/v1/")

    model='DeepSeek-R1-671B'
    

    with jsonlines.open('/hpc2hdd/home/qzheng219/yhuang/SecureCode/SecCodePLTPlus.jsonl', 'r') as f:
        for idx, data in enumerate(f):
            if idx >= args.start_idx and idx < args.start_idx + 100:
            
                print(f"Generating unit tests for task {count}")
                user_content = construct_user_content(data)
                response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": user_content},
                ],
                temperature=0.6,
                stream=False
                )
                result = parse_json_from_model_output(response.choices[0].message.content)
                if isinstance(result, dict):
                    result['task_id'] = data['task_id']
                    with jsonlines.open(f'SecCodePLTPlus_unittest_DeepSeek_{args.start_idx}.jsonl', 'a') as f:
                        f.write(result)
                else:
                    with open('SecCodePLTPlus_unittest_DeepSeek_error.txt', 'a') as f:
                        f.write('--------------------------------')
                        f.write(f"\n\n\n")
                        f.write(f"task_id: {data['task_id']}\n")
                        f.write(result)
                        f.write("\n")
            count += 1
                    
            
