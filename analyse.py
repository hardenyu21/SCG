import jsonlines


results = []
with jsonlines.open('/hpc2hdd/home/qzheng219/yhuang/SecureCode/results/vanilla/qwen25_14b/results.jsonl') as reader:
    for line in reader:
        results.append(line)

count_pass = 0
count_secure = 0
count_pass_secure = 0
accumulation = 0
count_hard_secure = 0
for result in results:
    if not(result['Severity'] * result['Confidence'] > 0):
        count_hard_secure += 1
    if result['pass_1']:
        count_pass += 1
    if result['secure_1']:
        count_secure += 1
    if result['pass_1'] and result['secure_1']:
        count_pass_secure += 1



print(f"total: {len(results)}")
print(f"count_pass: {count_pass}")
print(f"count_secure: {count_secure}")
print(f"count_pass_secure: {count_pass_secure}")
print(f"count_hard_secure: {count_hard_secure}")
