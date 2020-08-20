import os
import csv


file_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")


with open (file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # contents = file.read()
    header = next(csvreader)
    first_row= next(csvreader)

    for row in csvreader:

    total_months = 0
    Net_Change = []
    total_net = 0
    change_in_month = []

    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999]


# tracking the totals
    total_months = total_months + 1
    total_net = total_net + int(row[1])

# track net changes
    Change = int(row[1]) - previousnet
    previousnet = int(row[1])

    Net_Change = Net_Change + [Change]
    # Net_Change += [Change]
    change_in_month += [row[0]]

    #calculate greatest increase
    if Change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = Change
        





