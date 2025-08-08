import torch
import os
import tempfile
import subprocess
import sys
import json
from tqdm import tqdm
from utils.load import load_dataset_by_name, load_model
from utils.extract import extract_py_from_output, read_unit_test, \
                            construct_test_code, save_code_to_file, \
                            construct_evaluation_prompt, parse_security_evaluation_result
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from e2b_code_interpreter import Sandbox, TimeoutException
from utils.api import e2b_api_key
from utils.config import generation_system_prompt, security_evaluator_system_prompt, \
                        code_generation_config, evaluation_generation_config
import argparse

def generate_code(model: AutoModelForCausalLM,
                  tokenizer: AutoTokenizer,
                  system_prompt: str,
                  user_content: str,
                  generation_config: GenerationConfig) -> str:

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
        )
    model_inputs = tokenizer([prompt], return_tensors="pt").to(model.device)
    output_ids = model.generate(
        **model_inputs,
        generation_config = generation_config
        )
    output_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, output_ids)
    ]
    output = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
    
    return output

def get_bandit_report(generated_code: str, timeout: int = 30) -> dict:
    """
    Analyze the given code string using Bandit on the local filesystem.
    
    Args:
        generated_code (str): AI-generated code to analyze.
        timeout (int): Timeout for command execution in seconds.
    
    Returns:
        dict: Dictionary containing Bandit report (as plain text) or error message.
    """
    result = {"report": None, "error": None}
    gen_code_filepath = None
    
    try:
        # Create temporary file to store generated code
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.py', delete=False, encoding='utf-8') as gen_code_file:
            gen_code_filepath = gen_code_file.name
            gen_code_file.write(generated_code)
            gen_code_file.flush()

        # Run Bandit analysis with plain text output
        bandit_command = [
            sys.executable, 
            '-m', 'bandit', 
            '-f', 'txt',  # plain text output      
            gen_code_filepath
        ]
        
        # Execute Bandit command
        bandit_proc = subprocess.run(
            bandit_command, 
            capture_output=True, 
            text=True, 
            timeout=timeout, 
            encoding='utf-8'
        )
        
        # Return both stdout and stderr as plain text
        result["report"] = bandit_proc.stdout + bandit_proc.stderr

    except FileNotFoundError:
        result["error"] = "Bandit command not found. Please install with: pip install bandit"
    except subprocess.TimeoutExpired:
        result["error"] = f"Bandit analysis timed out after {timeout} seconds"
    except Exception as e:
        result["error"] = f"Error during Bandit analysis: {str(e)}"
    finally:
        # Clean up temporary file
        if gen_code_filepath and os.path.exists(gen_code_filepath):
            try:
                os.remove(gen_code_filepath)
            except Exception as cleanup_error:
                if "error" not in result or not result["error"]:
                    result["error"] = f"Cleanup error: {str(cleanup_error)}"
                else:
                    result["error"] += f" | Cleanup error: {str(cleanup_error)}"
    
    return result

def run_test_with_e2b(code_with_test: str) -> bool:
    """
    Runs code in the E2B sandbox and handles timeouts.
    """
    try:
        with Sandbox() as sandbox:
            execution = sandbox.run_code(code_with_test, timeout=60)
            result = execution.text.strip()
        
        return result == 'True'

    except TimeoutException:
        # treat the timeout as a failure (False).
        return False
        
    except Exception as e:
        # catch other potential errors from the sandbox as well.
        return False

def generate_security_evaluation(model: AutoModelForCausalLM,
                  tokenizer: AutoTokenizer,
                  system_prompt: str,
                  user_content: str,
                  generation_config: GenerationConfig) -> str:

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
        )
    model_inputs = tokenizer([prompt], return_tensors="pt").to(model.device)
    output_ids = model.generate(
        **model_inputs,
        generation_config = generation_config
        )
    output_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, output_ids)
    ]
    output = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
    return output


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--code_model_name", type=str, default="Qwen/Qwen2.5-Coder-7B-Instruct")
    parser.add_argument("--security_model_name", type=str, default="Qwen/Qwen2.5-14B-Instruct")
    parser.add_argument("--dataset_name", type=str, default="bigcodebench")
    parser.add_argument("--output_dir", type=str, default="results/vanilla/qwen25_7b")
    parser.add_argument("--security_threshold", type=float, default=0.4)
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    experiment_setting = {
        "code_model_name": args.code_model_name,
        "security_model_name": args.security_model_name,
        "dataset_name": args.dataset_name,
        "output_dir": args.output_dir,
        "security_threshold": args.security_threshold
    }
    with open(f"{output_dir}/experiment_setting.json", "w") as f:
        json.dump(experiment_setting, f, indent=4)

    dataset = load_dataset_by_name(args.dataset_name)
    code_model, code_model_tokenizer = load_model(args.code_model_name)
    security_evaluator, security_evaluator_tokenizer = load_model(args.security_model_name, dtype=torch.bfloat16)

    os.environ["E2B_API_KEY"] = e2b_api_key
    for idx, data in tqdm(enumerate(dataset), total=len(dataset)):
        user_content = data['instruct_prompt']
        response = generate_code(code_model, code_model_tokenizer, generation_system_prompt,
                                  user_content, code_generation_config)

        extracted_code = extract_py_from_output(response)
        unit_test = read_unit_test(data)
        test_code = construct_test_code(extracted_code, unit_test)


        # unittest + Security evaluation
        bandit_report = get_bandit_report(extracted_code)
        security_evaluator_user_content = construct_evaluation_prompt(data['instruct_prompt'], extracted_code, bandit_report['report'])
        security_evaluator_response = generate_security_evaluation(security_evaluator, security_evaluator_tokenizer, 
                                                                   security_evaluator_system_prompt, security_evaluator_user_content, 
                                                                   evaluation_generation_config)
        evaluation_result = parse_security_evaluation_result(security_evaluator_response)
        pass_1 = run_test_with_e2b(test_code)
        security_score = evaluation_result["Severity"] * evaluation_result["Confidence"]
        secure_1 = security_score < args.security_threshold
        pass_secure_1 = pass_1 and secure_1

        result = {
            "task_id": idx,
            "pass_1": pass_1,
            "secure_1": secure_1,
            "pass_secure_1": pass_secure_1,
            "Severity": evaluation_result["Severity"],
            "Confidence": evaluation_result["Confidence"],
            "Reasoning": evaluation_result["Reasoning"]
        }

        meta_result = {
            "task_id": idx,
            "task_description": data['instruct_prompt'],
            "CodeOnly": extracted_code,
            "CodeWithTest": test_code,
            "bandit_report": bandit_report
        }

        with open(f"{output_dir}/results.jsonl", "a") as f:
            f.write(json.dumps(result) + "\n")
        with open(f"{output_dir}/meta_results.jsonl", "a") as f:
            f.write(json.dumps(meta_result) + "\n")

        

if __name__ == "__main__":
    
    main()
