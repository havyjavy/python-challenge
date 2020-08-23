import os
import csv

file_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")


with open (file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")


    header = next(csvreader)
   
    candidates = []
    tvotes = 0

    for row in csvreader:
        candidate = str(row[2])
        candidates = candidate
        
    

        tvotes = tvotes + 1
        

    
    print(tvotes)
    print(candidates)

