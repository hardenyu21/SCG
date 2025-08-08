python hybrid/generate.py --model_name Qwen/Qwen2.5-Coder-7B-Instruct \
                          --output_dir results/vanilla/qwen25_7b \

python hybrid/generate.py --model_name Qwen/Qwen2.5-Coder-14B-Instruct \
                          --output_dir results/vanilla/qwen25_14b \

git add .
git commit -m "."
git push origin main