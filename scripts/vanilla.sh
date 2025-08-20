# python hybrid/generate.py --code_model_name Qwen/Qwen2.5-Coder-7B-Instruct \
#                           --output_dir results/vanilla/qwen25_7b 

# python hybrid/generate.py --code_model_name Qwen/Qwen2.5-Coder-14B-Instruct \
#                           --output_dir results/vanilla/qwen25_14b 

# echo "Qwen/Qwen2.5-Coder-3B-Instruct"
# python hybrid/generate.py --code_model_name Qwen/Qwen2.5-Coder-3B-Instruct \
#                           --output_dir results/vanilla/qwen25_3b 



echo "--------------------------------------------------"
echo "qwen2.5-coder-3B-Instruct-safecoder"
echo "--------------------------------------------------"
python hybrid/generate.py --code_model_name Qwen/Qwen2.5-Coder-3B-Instruct \
                          --code_model_path /hpc2hdd/home/qzheng219/yhuang/SecureCode/SafeCoder/trained/qwen25-3b-chat-lora-qwen25-3b-chat-safecoder/checkpoint-last \
                          --output_dir results/safecoder/qwen25_3b_safecoder 