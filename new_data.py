import jsonlines

dataset = []
with jsonlines.open('SecCodePLTPlus.jsonl') as reader:
    for line in reader:
        dataset.append(line)

print(len(dataset))
print(dataset[100])
