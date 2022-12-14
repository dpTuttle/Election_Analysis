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

#Initialize vote count to 0

total_votes = 0
candidate_picks = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(csvfilepath) as election_data:

#To do: perform analysis
#Read the file object with the reader function. 

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)

    for i in file_reader:
        total_votes +=1
        candidate_name = i[2]
        #if the candidate is not in the names already in the candidate list
        if candidate_name not in candidate_picks:
            #Add it to the list of candidates.
            candidate_picks.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#save the results to our text file
with open(outputfilepath, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"\n-----------------------\n"
        f"\nTotal Votes: {total_votes:,}\n"
        f"\n-------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)
        
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        print(candidate_results)

        txt_file.write(candidate_results)


    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)