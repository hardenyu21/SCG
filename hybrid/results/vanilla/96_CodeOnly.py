import csv
from collections import Counter

def task_func(csv_file, csv_delimiter):
    word_counter = Counter()
    
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=csv_delimiter)
        
        for row in csv_reader:
            for cell in row:
                word_counter[cell] += 1
    
    # Sort the words by frequency in descending order
    sorted_word_count = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
    
    return sorted_word_count