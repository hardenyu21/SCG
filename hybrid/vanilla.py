from dataset import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from tqdm import tqdm
import torch
if __name__ == "__main__":
    device = "cuda:0"
    dataset = load_dataset("bigcode/bigcodebench")['v0.1.4']
    model_name = "meta-llama/Llama-3.1-32B-Instruct"
    output_dir = "results/vanilla"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        attn_implementation="flash_attention_2"
    ).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    for idx, data in tqdm(enumerate(dataset), total=len(dataset)):
        prompt = data['instruct_prompt']
        messages = [
            {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
        )
        model_inputs = tokenizer([prompt], return_tensors="pt").to(model.device)
        generation_config = GenerationConfig(
        max_new_tokens=512,
        do_sample=False,
        temperature=None,
        top_p=None,
        top_k=None
)

        generated_ids = model.generate(
        **model_inputs,
        generation_config = generation_config
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        with open(f"test/vanilla_{idx}.txt", "a") as f:
            f.write(data['instruct_prompt'])
            f.write("\n")
            f.write(response)
            f.write("\n")
            f.write(data["entry_point"])
        if idx == 10:
            break