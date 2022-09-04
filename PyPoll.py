#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won. 
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote. 

# import datetime as dt

# now = dt.datetime.now()

# print("The time right now is ", now)

#Assign a variable for the file to load and the path.

import csv
import os

csvfilepath = os.path.join("Resources", "election_results.csv")

outputfilepath = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file.

with open(csvfilepath) as election_data:

#To do: perform analysis
#Read the file object with the reader function. 

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)

    print(headers)

