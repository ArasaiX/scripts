# Open csv (select trought prompt)
# Read and find the column we need (select trought prompt)
# iterate this column finding repeated values
# if the value is repeated write in another txt (or csv or json)
# print errors and another stuff

import csv
import json
import os.path
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Open csv (select through prompt) with tkinter
csv_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])

if not os.path.isfile(csv_path):
    print("File does not exist")
    exit()

# Read and find the column we need (select through prompt)
column_name = input("Enter the name of the column to search for: ")
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    if column_name not in rows[0]:
        print(f"Column {column_name} not found in CSV file")
        exit()
    values = [row[column_name] for row in rows]

# iterate this column finding repeated values
value_counts = {}
repeated_values = []

for value in values:
    if value not in value_counts:
        value_counts[value] = 1
    else:
        if value_counts[value] == 1:
            repeated_values.append(value)
        value_counts[value] += 1


# if the value is repeated write in another txt (or csv or json)
if repeated_values:
    output_file = input("Enter the name of the output file: ")
    # output_format = input("Enter the format of the output file (txt, csv, or json): ")
    # if output_format == "txt":
    with open(output_file, "w") as f:
        f.write("\n".join(repeated_values))
    # elif output_format == "csv":
    #     with open(output_file, "w") as f:
    #         writer = csv.writer(f)
    #         writer.writerow(["Repeated Values"])
    #         for value in repeated_values:
    #             writer.writerow([value])
    # elif output_format == "json":
    #     with open(output_file, "w") as f:
    #         json.dump({"Repeated Values": repeated_values}, f)