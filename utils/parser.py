import csv

def parse_icd_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        return [row for row in reader]
