# Description: This script is used to clean the CSV file with the revisions keeping only the Java files.

import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Clean the CSV file with the revisions keeping only the Java files')
parser.add_argument('input_file', type=str, help='CSV revisions input file')
parser.add_argument('output_file', type=str, help='CSV revisions output file')
args = parser.parse_args()

df = pd.read_csv(args.input_file)
df = df[df['entity'].str.endswith('.java')]
df.to_csv(args.output_file, index=False)