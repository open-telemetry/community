import csv
import os

VOTERS_ROLL_PATH = os.getenv('VOTERS_ROLL_PATH', './voters-roll.csv')
VOTERS_ROLL_HELIOS_PATH = os.getenv('VOTERS_ROLL_HELIOS_PATH', './voters-roll-helios.csv')

# Open the input and output CSV files
with open(VOTERS_ROLL_PATH, mode='r') as infile, open(VOTERS_ROLL_HELIOS_PATH, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Process each row in the input file
    for row in reader:
        if row is not None and len(row) > 0:
            writer.writerow(['github', row[0]])

print(f"Voters file for Helios Voting generated as {VOTERS_ROLL_HELIOS_PATH}")
