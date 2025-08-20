
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Tuple, Optional 
from datasets import load_dataset, Dataset
from peft import PeftModel
import os

def load_model(
    model_name: str, 
    dtype: Optional[torch.dtype] = None,
    use_flash_attention_2: bool = True
) -> Tuple[Optional[AutoModelForCausalLM], Optional[AutoTokenizer]]:
    
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    try:
        attn_impl = "flash_attention_2" if use_flash_attention_2 else None

        torch_dtype = dtype if dtype else "auto"
        

        if "deepseek" in model_name:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                trust_remote_code=True,
                torch_dtype=torch_dtype,
                device_map="auto",
                attn_implementation=attn_impl
            )
        else:
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch_dtype,
                device_map="auto",
                attn_implementation=attn_impl
        )
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        return model, tokenizer

    except Exception as e:
        print(f"Error loading model '{model_name}': {e}")
        return None, None
    
def load_lora_model_from_path(model_name: str, 
                              model_path: str, 
                              use_flash_attention_2: bool = False
) -> Tuple[Optional[AutoModelForCausalLM], Optional[AutoTokenizer]]:
    
    attn_impl = "flash_attention_2" if use_flash_attention_2 else None
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map='auto', attn_implementation=attn_impl)
    model.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(model, model_path)
    model = model.merge_and_unload()
    return model, tokenizer

def load_seccodeplt(version: str = "v0.1.4") -> Dataset:
    pass

def load_bigcodebench(version: str = "v0.1.4") -> Dataset:
    dataset = load_dataset("bigcode/bigcodebench")[version]
    return dataset

def load_dataset_by_name(dataset_name: str) -> Dataset:
    if dataset_name == "bigcodebench":
        return load_bigcodebench()
    elif dataset_name == "seccodeplt":
        return load_seccodeplt()
    else:
        raise ValueError(f"Dataset {dataset_name} not found")