import jsonlines


results = []
with jsonlines.open('results/vanilla/qwen25_14b/results.jsonl') as reader:
    for line in reader:
        results.append(line)

count_pass = 0
count_secure = 0
count_pass_secure = 0
accumulation = 0
for result in results:
    if result['pass_1']:
        count_pass += 1
    if result['secure_1']:
        count_secure += 1
    if result['pass_1'] and result['secure_1']:
        count_pass_secure += 1
    accumulation += result['Severity'] * result['Confidence']


print(f"total: {len(results)}")
print(f"count_pass: {count_pass}")
print(f"count_secure: {count_secure}")
print(f"count_pass_secure: {count_pass_secure}")
print(f'average security score: {accumulation / len(results)}')

meta_results = []
with jsonlines.open('results/vanilla/qwen25_14b/meta_results.jsonl') as reader:
    for line in reader:
        meta_results.append(line)
null_count = 0
for idx, meta_result in enumerate(meta_results):
    if meta_result['CodeOnly'] == '':
        null_count += 1
        print(idx)
    if idx == 1056:
        print(meta_result)
        break

print(f"null_count: {null_count}")