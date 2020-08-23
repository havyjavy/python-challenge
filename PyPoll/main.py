import os
import csv

file_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")


with open (file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")


    header = next(csvreader)
    first_row = next(csvreader)


    tvotes = 0

    for row in csvreader:

        
    

        tvotes = tvotes + 1
        

    
    print(tvotes)

