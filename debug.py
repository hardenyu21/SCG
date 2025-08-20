# import jsonlines
# import copy


# with jsonlines.open('SecCodePLTPlus.jsonl') as reader:
#     source_data = list(reader)

# print(len(source_data))
# paths = ['SecCodePLTPlus_unittest_DeepSeek.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_99.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_127.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_227.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_327.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_427.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_527.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_627.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_727.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_827.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_927.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_1027.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_1098.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_1198.jsonl',
#          'SecCodePLTPlus_unittest_DeepSeek_1298.jsonl',
# ]
# all_test_data = []
# for path in paths:
#     with jsonlines.open(path) as reader:
#         test_data = list(reader)
#     all_test_data.extend(test_data)
# new_dataset = []
# for data in source_data:
#     new_data = copy.deepcopy(data)
#     for app_data in all_test_data: 
#         if app_data['task_id'] == data['task_id']:
#             new_data['num_test_cases'] = app_data['num_test_cases']
#             new_data['test'] = app_data['test']
#             break
#     new_dataset.append(new_data)

# with jsonlines.open('SecCodePLTPlusPlus.jsonl', 'w') as writer:
#     for data in new_dataset:
#         writer.write(data)

# import jsonlines

# with jsonlines.open('bug.jsonl') as reader:
#     fix_data = list(reader)

# with jsonlines.open('SecCodePLTPlusPlus_fixed.jsonl') as reader:
#     source_data = list(reader)

# # Build a mapping from task_id to the corresponding fix record for O(1) lookups
# fix_by_task_id = {item['task_id']: item for item in fix_data}

# updated_count = 0
# unchanged_count = 0

# for item in source_data:
#     task_id = item.get('task_id')
#     if task_id in fix_by_task_id:
#         fix_item = fix_by_task_id[task_id]
#         if 'test' in fix_item:
#             item['test'] = fix_item['test']
#         if 'num_test_cases' in fix_item:
#             item['num_test_cases'] = fix_item['num_test_cases']
#         updated_count += 1
#     else:
#         unchanged_count += 1

# # Write the updated data to a new file to preserve the original
# with jsonlines.open('SecCodePLTPlusPlus_fixed_2.jsonl', 'w') as writer:
#     for record in source_data:
#         writer.write(record)

# print(f'Updated records: {updated_count}')
# print(f'Unchanged records (no fix found): {unchanged_count}')

# with jsonlines.open('SecCodePLTPlusPlus_fixed_2.jsonl', 'r') as reader:
#     data = list(reader)

# print(len(data))
# count = 0
# for idx, item in enumerate(data):
#     if 'test' not in item:
#         with open('error.txt', 'a') as f:
#             f.write(f'{str(idx)}: {item["task_id"]} \n')
#         count += 1
# print(count)



