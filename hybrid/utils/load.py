
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Tuple, Optional 
from datasets import load_dataset, Dataset

def load_model(
    model_name: str, 
    dtype: Optional[torch.dtype] = None,
    use_flash_attention_2: bool = True
) -> Tuple[Optional[AutoModelForCausalLM], Optional[AutoTokenizer]]:
    
    try:
        attn_impl = "flash_attention_2" if use_flash_attention_2 else None

        torch_dtype = dtype if dtype else "auto"

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