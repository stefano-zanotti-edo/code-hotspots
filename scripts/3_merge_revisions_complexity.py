# Description: Merge revisions and complexity data into a single CSV file.
# This script reads two CSV files, one with the revisions data and another with the complexity data.
# The script merges the data and saves it to a new CSV file with the following columns:
# - entity
# - n-revs
# - complexity
# The script receives the paths to the revisions and complexity files and the output file as arguments.

import csv
import argparse

parser = argparse.ArgumentParser(description='Merge revisions and complexity data into a single CSV file.')
parser.add_argument('revisions_file', type=str, help='CSV file with revisions data')
parser.add_argument('complexity_file', type=str, help='CSV file with complexity data')
parser.add_argument('output_file', type=str, help='CSV output file')
args = parser.parse_args()

revisions = {}
# read the revisions file
with open(args.revisions_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        entity, n_revs = row
        revisions[entity] = int(n_revs)

complexities = {}
# read the complexity file
with open(args.complexity_file, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        language, filename, blank, comment, code = row
        complexities[filename] = int(code)

merged_data = []
# merge the data
for entity, n_revs in revisions.items():
    complexity = complexities.get(entity, 0)
    merged_data.append((entity, n_revs, complexity))

merged_data.sort(key=lambda x: (x[1], x[2]), reverse=True)

with open(args.output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['entity', 'n-revs', 'complexity'])
    for row in merged_data:
        writer.writerow(row)

print(f"Data merged in file {args.output_file}")