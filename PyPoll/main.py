import os
import csv

file_path = os.path.join("..", "PyPoll", "budget_data.csv")

with open (file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    