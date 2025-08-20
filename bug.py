import jsonlines

with jsonlines.open('bug.jsonl') as reader:
    fix_data = list(reader)

with jsonlines.open('SecCodePLTPlusPlus_fixed.jsonl') as reader:
    source_data = list(reader)

# Build a mapping from task_id to the corresponding fix record for O(1) lookups
fix_by_task_id = {item['task_id']: item for item in fix_data}

updated_count = 0
unchanged_count = 0

for item in source_data:
    task_id = item.get('task_id')
    if task_id in fix_by_task_id:
        fix_item = fix_by_task_id[task_id]
        if 'test' in fix_item:
            item['test'] = fix_item['test']
        if 'num_test_cases' in fix_item:
            item['num_test_cases'] = fix_item['num_test_cases']
        updated_count += 1
    else:
        unchanged_count += 1

# Write the updated data to a new file to preserve the original
with jsonlines.open('SecCodePLTPlusPlus_fixed_2.jsonl', 'w') as writer:
    for record in source_data:
        writer.write(record)

print(f'Updated records: {updated_count}')
print(f'Unchanged records (no fix found): {unchanged_count}')

