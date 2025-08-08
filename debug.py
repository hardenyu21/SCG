


from hybrid.utils.load import load_dataset_by_name
from transformers import AutoModelForCausalLM, AutoTokenizer
from hybrid.generate import generate_code, extract_py_from_output
from hybrid.utils.config import code_generation_config, generation_system_prompt

dataset = load_dataset_by_name("bigcodebench")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

for idx, data in enumerate(dataset):
    if idx == 274:
        user_content = data['instruct_prompt']
        response = generate_code(model, tokenizer, generation_system_prompt, user_content, code_generation_config)
        print(response)
        print(extract_py_from_output(response))
        break