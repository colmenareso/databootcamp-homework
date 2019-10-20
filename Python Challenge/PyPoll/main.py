# Set up dependencies

import pandas as pd
import os as os

# Initialize variabales and list

# List of candidate names
name_list = []

# Creating a counter for the votes for each candidate in the list
vote = 0

# List that will store the votes of each of the candidates
votebyname = []

#  Creating a counter for the percentage of the overall vote count for each candidate in the list
percent = 0

# List that will store the percentage of votes of each of the candidates
percentbyname = []

# Import the raw data into a DataFrame

csvpath = ("Resources/election_data.csv")
election_poll_pd = pd.read_csv(csvpath)

# Calculate the total number of votes
total_vote = len(election_poll_pd["Candidate"])

# Creating a list of unique candidates

name_list= election_poll_pd['Candidate'].unique()

# Loop to slice the original file by candidate name and count the number of votes for each candidate
# Store the votes based on the candidate name in the votebyname list

for x in range(len(name_list)):
    election_poll_byname = election_poll_pd.loc[election_poll_pd["Candidate"] == name_list[x], :]
    vote = len(election_poll_byname["Candidate"])
    votebyname.append(vote)

# Loop to calculate the percentage of votes for each of the candidates based on the votebyname list
# Store the votes based on the candidate name in the votebyname list

for x in range(len(name_list)):
    percent = "{:.3%}".format(votebyname[x] / total_vote)
    percentbyname.append(percent)

# Assigning the values to candidate's name, votes and percentage

name1 = name_list[0]
vote1 = votebyname[0]
percent1 = percentbyname[0]

name2 = name_list[1]
vote2 = votebyname[1]
percent2 = percentbyname[1]

name3 = name_list[2]
vote3 = votebyname[2]
percent3 = percentbyname[2]

name4 = name_list[3]
vote4 = votebyname[3]
percent4 = percentbyname[3]

# Determining the winner or whether there is a tie

if ((vote1 > vote2)  & (vote1 > vote3) & (vote1 > vote4)):
    winner = name1
elif ((vote2> vote1)  & (vote2 > vote3) & (vote2 > vote4)):
    winner = name2
elif ((vote3 > vote1)  & (vote3 > vote2) & (vote3 > vote4)):
    winner = name3
elif ((vote4 > vote1)  & (vote4 > vote2) & (vote4 > vote3)):
    winner = name4
else:
    winner = "tied"

# Printing terminal according to the output
    
if winner != "tied":
    # Printing terminal to announce the voting count and thew winner
    output1 = (
    f"Election Results\n"
    f" \n"
    f"---------------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"---------------------------------\n"
    f"{name1}: {percent1} ({vote1})\n"
    f"{name2}: {percent2} ({vote2})\n"
    f"{name3}: {percent3} ({vote3})\n"
    f"{name4}: {percent4} ({vote4})\n"
    f"---------------------------------\n"
    f" \n"
    f"Winner: {winner}\n"
    f" \n"
    f"---------------------------------\n"
    )
    print(output1)
    # Writing output text file with vote results with a winner
    
    file_to_output = os.path.join("Output", "Election Results.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output1)

else:
    output2 = (
    f"-----------------------------------\n"
    f"You might need to ask for a recount\n"
    f"Election Results\n"
    f" \n"
    f"---------------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"---------------------------------\n"
    f"{name1}: {percent1} ({vote1})\n"
    f"{name2}: {percent2} ({vote2})\n"
    f"{name3}: {percent3} ({vote3})\n"
    f"{name4}: {percent4} ({vote4})\n"
    f"---------------------------------\n"
    )
    print(output2)
    # Writing output text file with vote results announcing a tie vote
    
    file_to_output = os.path.join("Output", "Election Results.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output2)