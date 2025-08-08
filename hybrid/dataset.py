from datasets import load_dataset
import json
import copy
from utils.load import load_dataset_by_name
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




if __name__ == "__main__":

    original_dataset = load_dataset("Virtue-AI-HUB/SecCodePLT")['insecure_coding']
    bigcodebench = load_dataset_by_name("bigcodebench")
    for data in original_dataset:
        new_data = copy.deepcopy(data)
        new_data['instruct_prompt'], new_data['instruct_prompt_wo_security'] = construct_prompt(data)
        new_data['canonical_solution'] = construct_ground_truth(data)
        print(new_data)
        break

    # processed_dataset = []
    # select_task = {}
    # select_id = []
    # with open('answer.json', 'r') as f:
    #     answer = json.load(f)
    # for data in answer:
    #     select_task[data['task_id']] = data
    #     select_id.append(data['task_id'])
    # for data in original_dataset:
    #     new_data = copy.deepcopy(data)
    #     if data['id'] in select_id:
    #         id = data['id']
    #         prompt = construct_prompt(data)
    #         new_data['prompt'] = prompt
    #         test_results = select_task[id]['results']
    #         test_cases = []
    #         for test_case in test_results:
    #             print(test_case)
    #             new_test_case = {}
    #             new_test_case['input'] = test_case['params']
    #             new_test_case['output'] = test_case['result']
    #             test_cases.append(new_test_case)
    #         new_data['test_cases'] = test_cases
    #         processed_dataset.append(new_data)
    # with open('processed_dataset.json', 'w') as f:
    #     json.dump(processed_dataset, f, indent=4)
    # print("Done!")
