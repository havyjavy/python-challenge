import os
import csv


file_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")


with open (file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # contents = file.read()
    header = next(csvreader)
    # first_row= next(csvreader)

    
    total_months = 0
    total_net = 0
    previousnet = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999]

    for row in csvreader:

        Net_Change = []
        change_in_month = []




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
        

        if Change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Change


   
    
    print("Financial Analysis")
    print("-----------------------------")


    print(f"Total Months: {str(total_months)}")
    print(f"Total: {str(total_net)}")
    print(f"Greatest Decrease in Profits: {str(greatest_decrease)}")
    print(f"Greatest Increase in Profits: {str(greatest_increase)}")
    
    




