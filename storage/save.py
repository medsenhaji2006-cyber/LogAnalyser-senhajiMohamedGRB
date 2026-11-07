import csv
import os

def save_records(all_records, path='./storage/records.csv'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not all_records:
        return
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_records[0].keys())
        writer.writeheader()
        writer.writerows(all_records)

def save_rejected(rejected, path='./storage/rejected.log'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for line in rejected:
            f.write(line + '\n')