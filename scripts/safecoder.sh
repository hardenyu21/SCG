

##train
##python scripts/train.py --pretrain_name qwen25-3b-chat --output_name qwen25-3b-chat-safecoder --datasets sec-desc sec-new-desc

# echo "--------------------------------------------------"
# echo "qwen2.5-coder-3B-Instruct-safecoder"
# echo "--------------------------------------------------"

# python hybrid/generate.py \
#     --code_model_name Qwen/Qwen2.5-Coder-3B-Instruct \
#     --code_model_path /hpc2hdd/home/qzheng219/yhuang/SecureCode/SafeCoder/trained/qwen25-3b-chat-lora-qwen25-3b-chat-safecoder/checkpoint-last \
#     --output_dir results/safecoder2/qwen25_3b_safecoder  



# echo "--------------------------------------------------"
# echo "qwen2.5-coder-7B-Instruct-safecoder"
# echo "--------------------------------------------------"
# python hybrid/generate.py \
#     --code_model_name Qwen/Qwen2.5-Coder-7B-Instruct \
#     --code_model_path /hpc2hdd/home/qzheng219/yhuang/SecureCode/SafeCoder/trained/qwen25-7b-chat-lora-qwen25-7b-chat-safecoder/checkpoint-last \
#     --output_dir results/safecoder2/qwen25_7b_safecoder


##train
#python scripts/train.py --pretrain_name qwen25-14b-chat --output_name qwen25-14b-chat-safecoder --datasets sec-desc sec-new-desc

echo "--------------------------------------------------"
echo "qwen2.5-coder-14B-Instruct-safecoder"
echo "--------------------------------------------------"
python hybrid/generate.py \
    --code_model_name Qwen/Qwen2.5-Coder-14B-Instruct \
    --code_model_path /hpc2hdd/home/qzheng219/yhuang/SecureCode/SafeCoder/trained/qwen25-14b-chat-lora-qwen25-14b-chat-safecoder/checkpoint-last \
    --output_dir results/safecoder2/qwen25_14b_safecoder